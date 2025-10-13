import logging
from typing import Any, Dict, List

from delta.tables import DeltaTable
from pyspark.sql import DataFrame, SparkSession
from pyspark.sql.types import StructType
from utils.access import grant_access_to_bronze
from utils.utils import add_metadata_columns, generate_batch_id

logger = logging.getLogger(__name__)


def ingest_bronze_customer_data(
    spark: SparkSession,
    config: Dict[str, Any],
    schema: StructType,
    file_format: str
) -> List[DataFrame]:
    """
    Ingests raw customer data into the Bronze
    Delta Table using Auto Loader.
    """
    batch_id = generate_batch_id()
    queries = []

    input_paths = (
        config["input_path"]
        if isinstance(config["input_path"], list)
        else [config["input_path"]]
    )

    try:
        if not DeltaTable.isDeltaTable(spark, config["output_path"]):
            logger.info(
                f"Table not found at {config['output_path']}. "
                "Creating Table..."
            )

            spark.sql(f"""
                CREATE TABLE IF NOT EXISTS {config['catalog']}.{config['database']}.bronze
                USING DELTA
                LOCATION '{config['output_path']}'
            """)

            grant_access_to_bronze(spark, config['catalog'], config['database'])
        else:
            pass
    except Exception as e:
        logger.error(f"Failed to check/create Delta table: {e}")
        raise

    for path in input_paths:
        logger.info(f"Starting ingestion from path: {path}")

        try:
            if spark.read.format(file_format) \
                    .load(path) \
                    .limit(1) \
                    .rdd.isEmpty():
                logger.warning(
                    f"No files found in path: {path}, skipping ingestion."
                )
                continue
            else:
                pass
        except Exception as e:
            logger.warning(
                f"Path not found or empty: {path} ({e}), skipping ingestion."
            )
            continue

        try:
            df = (
                spark.readStream
                .format("cloudFiles")
                .option("cloudFiles.format", file_format)
                .option("header", "true")
                .schema(schema)
                .load(path)
            )

            df = add_metadata_columns(df, batch_id)

            path_name = path.rstrip("/").split("/")[-1]
            checkpoint_path_for_path = (
                f"{config['checkpoint_path']}/"
                f"{path_name}"
            )

            query = (
                df.writeStream
                .format("delta")
                .outputMode("append")
                .trigger(once=True)
                .option("checkpointLocation", checkpoint_path_for_path)
                .start(config["output_path"])
            )

            query.awaitTermination()
            queries.append(query)
        except Exception as e:
            logger.error(f"Failed ingestion from path {path}: {e}")

    return queries

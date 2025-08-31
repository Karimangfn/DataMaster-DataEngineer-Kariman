import logging

from typing import Dict, List
from pyspark.sql import DataFrame, SparkSession
from pyspark.sql.types import StructType
from utils.utils import add_metadata_columns, generate_batch_id

logger = logging.getLogger(__name__)


def ingest_bronze_customer_data(
    spark: SparkSession,
    config: Dict[str, any],
    schema: StructType,
    file_format: str
) -> List[DataFrame]:
    """
    Ingests raw customer data into the Bronze Delta Lake table using Auto Loader.
    Supports multiple input paths.

    Args:
        spark (SparkSession): The active Spark session.
        config (dict): Configuration dictionary containing:
            - input_path (list of str): Paths to the raw data in cloud storage.
            - output_path (str): Destination path for the Bronze Delta table.
            - checkpoint_path (str): Path to store checkpoints.
        schema (StructType): Expected schema of the input dataset.
        file_format (str): File format to read (e.g., "csv").

    Returns:
        List[DataFrame]: The DataFrames that were ingested.
    """
    batch_id = generate_batch_id()
    queries = []

    input_paths = config["input_path"] if isinstance(config["input_path"], list) else [config["input_path"]]

    for path in input_paths:
        logger.info(f"Starting ingestion from path: {path}")

        df = (
            spark.readStream
            .format("cloudFiles")
            .option("cloudFiles.format", file_format)
            .option("header", "true")
            .schema(schema)
            .load(path)
        )

        df = add_metadata_columns(df, batch_id)

        query = (
            df.writeStream
            .format("delta")
            .outputMode("append")
            .trigger(once=True)
            .option("checkpointLocation", config["checkpoint_path"])
            .start(config["output_path"])
        )

        queries.append(query)

    return queries

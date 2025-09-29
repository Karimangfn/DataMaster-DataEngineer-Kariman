import logging

from typing import Any, Dict
from pyspark.sql import SparkSession
from utils.utils import add_purchase_month_column, aggregate_purchase_metrics

logger = logging.getLogger(__name__)


def transform_gold(
    spark: SparkSession,
    config: Dict[str, str]
) -> None:
    """
    Reads Silver layer data as batch Delta, adds purchase_month column,
    aggregates purchase metrics by store location and month, and writes
    results to Gold layer as batch Delta.

    Args:
        spark (SparkSession): Spark session object.
        config: Dictionary with all pipeline configurations.

    Returns:
        None
    """
    try:
        logger.info(f"Reading data from Silver path: {config['silver_path']}")
        df = spark.read.format("delta").load(config["silver_path"])

        logger.info("Adding purchase_month column...")
        df = add_purchase_month_column(df)

        logger.info(
            "Aggregating purchase metrics..."
        )
        df_agg = aggregate_purchase_metrics(
            df, ["store_location", "purchase_month"]
        )

        logger.info(f"Writing aggregated data to Gold path: {config['gold_path']}")
        df_agg.write \
            .format("delta") \
            .mode("overwrite") \
            .option("path", config["gold_path"]) \
            .saveAsTable(f"{config['catalog']}.{config['database']}.gold")
    except Exception as e:
        logger.error(f"Error during Gold transformation: {e}")
        raise

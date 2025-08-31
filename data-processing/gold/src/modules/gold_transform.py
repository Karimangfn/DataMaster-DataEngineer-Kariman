import logging

from pyspark.sql import SparkSession
from utils.utils import add_purchase_month_column, aggregate_purchase_metrics

logger = logging.getLogger(__name__)


def transform_gold(
    spark: SparkSession,
    silver_path: str,
    gold_path: str
) -> None:
    """
    Reads Silver layer data as batch Delta, adds purchase_month column,
    aggregates purchase metrics by store location and month, and writes
    results to Gold layer as batch Delta.

    Args:
        spark (SparkSession): Spark session object.
        silver_path (str): Path to Silver Delta table.
        gold_path (str): Output path for Gold Delta table.

    Returns:
        None
    """
    try:
        logger.info(f"Reading data from Silver path: {silver_path}")
        df = spark.read.format("delta").load(silver_path)

        logger.info("Adding purchase_month column...")
        df = add_purchase_month_column(df)

        logger.info(
            "Aggregating purchase metrics..."
        )
        df_agg = aggregate_purchase_metrics(
            df, ["store_location", "purchase_month"]
        )
        logger.info(f"Writing aggregated data to Gold path: {gold_path}")
        df_agg.write.format("delta").mode("overwrite").save(gold_path)
    except Exception as e:
        logger.error(f"Error during Gold transformation: {e}")
        raise

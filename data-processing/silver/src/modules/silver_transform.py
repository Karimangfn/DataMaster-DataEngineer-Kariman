import logging

from typing import Any, Dict, List
from pyspark.sql import SparkSession
from utils.utils import (add_high_value_flag, clean_and_cast_columns,
                         deduplicate, mask_sensitive_data)

logger = logging.getLogger(__name__)


def transform_silver(
    spark: SparkSession,
    config: Dict[str, Any]
) -> None:
    """
    Reads Bronze data in batch, cleans and masks sensitive data,
    removes duplicates, adds a high value purchase flag,
    and writes to the Silver layer.

    Args:
        spark: SparkSession object.
        config: Dictionary with all pipeline configurations.

    Returns:
        None
    """
    try:
        logger.info(f"Reading data from Bronze path: {config['bronze_path']}")
        df = spark.read.format("delta").load(config["bronze_path"])

        logger.info("Cleaning and casting columns...")
        df = clean_and_cast_columns(df)

        logger.info("Deduplicating records...")
        df = deduplicate(df)

        logger.info("Masking sensitive data...")
        df = mask_sensitive_data(df)

        logger.info("Adding high value purchase flag...")
        df = add_high_value_flag(df)

        logger.info(f"Writing transformed data to Silver path: {config['silver_path']}")
        df.write \
          .format("delta") \
          .mode("append") \
          .option("path", config["silver_path"]) \
          .saveAsTable(f"{config['catalog']}.{config['database']}.silver")
    except Exception as e:
        logger.error(f"Error during Silver transformation: {e}")
        raise

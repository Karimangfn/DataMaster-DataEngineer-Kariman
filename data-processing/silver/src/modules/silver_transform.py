import logging
import sys

from pyspark.sql import SparkSession
from modules.utils import (
    clean_and_cast_columns,
    deduplicate,
    mask_sensitive_data,
    add_high_value_flag,
)

logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def transform_silver(spark: SparkSession, bronze_path: str, silver_path: str) -> None:
    """
    Reads Bronze data in batch, cleans and masks sensitive data,
    removes duplicates, adds a high value purchase flag,
    and writes to the Silver layer.

    Args:
        spark: SparkSession object.
        bronze_path: Path to the Bronze data folder.
        silver_path: Output path for the Silver Delta table.

    Returns:
        None
    """
    try:
        logger.info(f"Reading data from Bronze path: {bronze_path}")
        df = spark.read.format("delta").load(bronze_path)
        
        logger.info("Cleaning and casting columns...")
        df = clean_and_cast_columns(df)
        
        logger.info("Deduplicating records...")
        df = deduplicate(df)
        
        logger.info("Masking sensitive data...")
        df = mask_sensitive_data(df)
        
        logger.info("Adding high value purchase flag...")
        df = add_high_value_flag(df)
    
        logger.info(f"Writing transformed data to Silver path: {silver_path}")
        df.write.format("delta").mode("append").save(silver_path)
    except Exception as e:
        logger.error(f"Error during Silver transformation: {e}")
        raise

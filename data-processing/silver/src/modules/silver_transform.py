from pyspark.sql import SparkSession
from modules.utils import (
    clean_and_cast_columns,
    deduplicate,
    mask_sensitive_data,
    add_high_value_flag,
)

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
    df = spark.read.format("delta").load(bronze_path)
    df = clean_and_cast_columns(df)
    df = deduplicate(df)
    df = mask_sensitive_data(df)
    df = add_high_value_flag(df)
    df.write.format("delta").mode("append").save(silver_path)

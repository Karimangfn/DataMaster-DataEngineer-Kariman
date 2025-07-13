import uuid

from pyspark.sql.functions import current_timestamp, input_file_name, lit


def generate_batch_id():
    """
    Generates a unique UUID to represent a batch ID used for 
    tracking data ingestion into the raw/bronze layer.

    Returns:
        str: UUID string.
    """
    return str(uuid.uuid4())


def add_metadata_columns(df, batch_id):
    """
    Adds metadata columns to the DataFrame for lineage and traceability:
    - source_file_name: full path of the source file.
    - ingestion_timestamp: timestamp of data ingestion.
    - raw_ingestion_id: unique batch identifier.

    Args:
        df (DataFrame): Input Spark DataFrame.
        batch_id (str): Batch UUID generated at the beginning of the pipeline.

    Returns:
        DataFrame: DataFrame with metadata columns added.
    """
    return (
        df.withColumn("source_file_name", input_file_name())
          .withColumn("ingestion_timestamp", current_timestamp())
          .withColumn("raw_ingestion_id", lit(batch_id))
    )


def detect_format_from_extension(file_name):
    """
    Detects the file format based on the file extension.

    Supported formats:
    - .csv
    - .json
    - .parquet

    Args:
        file_name (str): Name or full path of the file.

    Returns:
        str: Detected format ("csv", "json", or "parquet").

    Raises:
        ValueError: If the file extension is not supported.
    """
    format_map = {
        ".csv": "csv",
        ".json": "json",
        ".parquet": "parquet"
    }

    for ext, fmt in format_map.items():
        if file_name.endswith(ext):
            return fmt

    raise ValueError(f"Unsupported file format: {file_name}")

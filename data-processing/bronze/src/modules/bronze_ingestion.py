from utils.utils import add_metadata_columns, generate_batch_id


def ingest_bronze_customer_data(spark, config, schema, file_format):
    """
    Ingests raw customer data into the Bronze Delta Lake table using Auto Loader.

    Args:
        spark (SparkSession): The active Spark session.
        config (dict): Configuration dictionary containing:
            - input_path (str): Path to the raw data in cloud storage.
            - output_path (str): Destination path for the Bronze Delta table.
            - checkpoint_path (str): Path to store streaming checkpoints.
        schema (StructType): Expected schema of the input dataset.
        file_format (str): File format to read (e.g., "csv", "json", "parquet").

    Returns:
        StreamingQuery: A reference to the running writeStream query.
    """
    batch_id = generate_batch_id()

    df = (
        spark.readStream
            .format("cloudFiles")
            .option("cloudFiles.format", file_format)
            .option("header", "true")
            .schema(schema)
            .load(config["input_path"])
    )

    df = add_metadata_columns(df, batch_id)

    return (
        df.writeStream
          .format("delta")
          .outputMode("append")
          .option("checkpointLocation", config["checkpoint_path"])
          .start(config["output_path"])
    )

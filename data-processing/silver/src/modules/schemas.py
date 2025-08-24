from pyspark.sql.types import (BooleanType, DateType, DoubleType, StringType,
                               StructField, StructType, TimestampType)


def get_silver_schema() -> StructType:
    """
    Returns the schema for the Silver layer customer
    data with masked sensitive information and
    metadata columns.

    Fields:
        - customer_id (StringType): Unique identifier of the customer.
        - first_name (StringType): Customer's first name.
        - last_name (StringType): Customer's last name.
        - email (StringType): Customer's email address.
        - purchase_date (DateType): Date of purchase.
        - total_amount (DoubleType): Total purchase amount.
        - product (StringType): Product name.
        - store_location (StringType): Store location.
        - cpf_masked (StringType): Masked CPF (Brazilian tax ID).
        - credit_card_masked (StringType): Masked credit card number.
        - source_file_name (StringType): Name of source file.
        - ingestion_timestamp (TimestampType): Timestamp of ingestion.
        - raw_ingestion_id (StringType): Batch ingestion identifier.
        - high_value_purchase (BooleanType): Flag for high value purchases.
    """
    return StructType([
        StructField("customer_id", StringType(), True),
        StructField("first_name", StringType(), True),
        StructField("last_name", StringType(), True),
        StructField("email", StringType(), True),
        StructField("purchase_date", DateType(), True),
        StructField("total_amount", DoubleType(), True),
        StructField("product", StringType(), True),
        StructField("store_location", StringType(), True),
        StructField("cpf_masked", StringType(), True),
        StructField("credit_card_masked", StringType(), True),
        StructField("source_file_name", StringType(), True),
        StructField("ingestion_timestamp", TimestampType(), True),
        StructField("raw_ingestion_id", StringType(), True),
        StructField("high_value_purchase", BooleanType(), True),
    ])

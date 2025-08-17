from pyspark.sql.types import StringType, StructField, StructType


def get_customer_schema():
    """
    Returns the expected schema for raw customer data.

    This schema is used during ingestion to enforce a consistent
    structure for input files of varying formats (CSV, JSON, Parquet).

    Fields:
        - customer_id (string): Unique identifier for the customer.
        - first_name (string): Customer's first name.
        - last_name (string): Customer's last name.
        - email (string): Customer's email address.
        - purchase_date (string): Date of purchase (raw format).
        - total_amount (string): Total amount of the purchase.
        - product (string): Name or ID of the purchased product.
        - store_location (string): Physical store where the purchase occurred.
        - cpf (string): Customer's Brazilian CPF (tax ID).
        - credit_card_number (string): Customer's credit card number.

    Returns:
        StructType: A Spark StructType object defining the schema.
    """
    return StructType([
        StructField("customer_id", StringType(), True),
        StructField("first_name", StringType(), True),
        StructField("last_name", StringType(), True),
        StructField("email", StringType(), True),
        StructField("purchase_date", StringType(), True),
        StructField("total_amount", StringType(), True),
        StructField("product", StringType(), True),
        StructField("store_location", StringType(), True),
        StructField("cpf", StringType(), True),
        StructField("credit_card_number", StringType(), True)
    ])

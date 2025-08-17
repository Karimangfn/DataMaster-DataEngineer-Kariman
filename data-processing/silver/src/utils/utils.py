import re

from pyspark.sql.functions import col, row_number, sha2, to_date, udf
from pyspark.sql.types import BooleanType
from pyspark.sql.window import Window


def validate_email(df, email_col="email"):
    """
    Validates email addresses in the specified column using a regex pattern.

    Args:
        df: Spark DataFrame containing the data.
        email_col (str): Name of the email column to validate.

    Returns:
        DataFrame with an additional boolean column 'is_email_valid' indicating
        validity of the email addresses.
    """
    email_regex = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    def is_valid_email(email):
        if email is None:
            return False
        return re.match(email_regex, email) is not None

    is_valid_email_udf = udf(is_valid_email, BooleanType())

    return df.withColumn("is_email_valid", is_valid_email_udf(df[email_col]))


def clean_and_cast_columns(df):
    """
    Converts 'purchase_date' to date type and casts 'total_amount' to double.

    Args:
        df: Input DataFrame.

    Returns:
        DataFrame with updated column types.
    """
    return (
        df.withColumn("purchase_date",
                      to_date(col("purchase_date"), "M/d/yyyy"))
          .withColumn("total_amount",
                      col("total_amount").cast("double"))
    )


def deduplicate(df):
    """
    Removes duplicates keeping the latest record
    per customer_id and purchase_date, based on
    ingestion_timestamp.

    Args:
        df: Input DataFrame.

    Returns:
        Deduplicated DataFrame.
    """
    window_spec = Window.partitionBy("customer_id", "purchase_date").orderBy(
        col("ingestion_timestamp").desc()
    )
    return (
        df.withColumn("row_num", row_number().over(window_spec))
          .filter(col("row_num") == 1)
          .drop("row_num")
    )


def mask_sensitive_data(df):
    """
    Masks sensitive columns 'cpf' and 'credit_card_number' using SHA-256 hash.

    Args:
        df: Input DataFrame.

    Returns:
        DataFrame with masked columns and original columns dropped.
    """
    return (
        df.withColumn("cpf_masked", sha2(col("cpf"), 256))
          .withColumn("credit_card_masked",
                      sha2(col("credit_card_number"), 256))
          .drop("cpf")
          .drop("credit_card_number")
    )


def add_high_value_flag(df, amount_col="total_amount", threshold=5):
    """
    Adds a boolean flag for high value purchases where
    amount exceeds threshold.

    Args:
        df: Input DataFrame.
        amount_col (str): Column name for amount.
        threshold (float): Threshold for high value.

    Returns:
        DataFrame with 'high_value_purchase' boolean column.
    """
    return df.withColumn(
        "high_value_purchase",
        (col(amount_col) > threshold).cast("boolean")
    )

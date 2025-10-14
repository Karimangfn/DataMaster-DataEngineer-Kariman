import re

from pyspark.sql import DataFrame
from pyspark.sql.functions import coalesce, regexp_replace, col, row_number, sha2, to_date, udf
from pyspark.sql.types import BooleanType
from pyspark.sql.window import Window


def validate_email(
    df: DataFrame,
    email_col: str = "email"
) -> DataFrame:
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
    Cleans and casts columns to proper types.
    Handles $, commas, and multiple date formats.
    """
    df = df.withColumn(
        "total_amount",
        regexp_replace(col("total_amount"), "[$,]", "").cast("double")
    )

    df = df.withColumn(
        "purchase_date",
        coalesce(
            to_date(col("purchase_date"), "M/d/yyyy"),
            to_date(col("purchase_date"), "MM/dd/yyyy"),
            to_date(col("purchase_date"), "yyyy-MM-dd")
        )
    )

    return df

def deduplicate(df: DataFrame) -> DataFrame:
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


def mask_sensitive_data(df: DataFrame) -> DataFrame:
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


def add_high_value_flag(
    df: DataFrame,
    amount_col: str = "total_amount",
    threshold: float = 5
) -> DataFrame:
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

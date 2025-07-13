from pyspark.sql.types import *


def get_gold_schema():
    """
    Returns the schema for the Gold layer aggregated customer purchase data.

    Fields:
        - store_location (StringType): Store location identifier.
        - purchase_month (StringType): Purchase month in 'yyyy-MM' format.
        - total_purchases (IntegerType): Total number of purchases.
        - total_revenue (DoubleType): Sum of total amount spent.
        - average_purchase_value (DoubleType): Average purchase value.
        - high_value_purchases (IntegerType): Count of high value purchases.
    """
    return StructType([
        StructField("store_location", StringType(), True),
        StructField("purchase_month", StringType(), True),
        StructField("total_purchases", IntegerType(), True),
        StructField("total_revenue", DoubleType(), True),
        StructField("average_purchase_value", DoubleType(), True),
        StructField("high_value_purchases", IntegerType(), True
        )
    ])

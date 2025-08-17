from pyspark.sql.functions import avg, col, count, date_format, expr
from pyspark.sql.functions import sum as _sum


def add_purchase_month_column(df, date_col="purchase_date"):
    """
    Adds a purchase_month column formatted as yyyy-MM from a date column.
    """
    return df.withColumn("purchase_month",
                         date_format(col(date_col), "yyyy-MM"))


def aggregate_purchase_metrics(df, group_cols):
    """
    Aggregates purchase metrics: total purchases, total revenue,
    average purchase value, and count of high value purchases.

    Args:
        df: Input DataFrame.
        group_cols: List of columns to group by.

    Returns:
        Aggregated DataFrame.
    """
    return (
        df.groupBy(*group_cols)
          .agg(
              count("*").alias("total_purchases"),
              _sum("total_amount").alias("total_revenue"),
              avg("total_amount").alias("average_purchase_value"),
              _sum(
                  expr("CASE WHEN high_value_purchase THEN 1 ELSE 0 END")
              ).alias("high_value_purchases"))
    )

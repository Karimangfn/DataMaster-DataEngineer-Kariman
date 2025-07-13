from src.utils.utils import add_purchase_month_column, aggregate_purchase_metrics

def transform_gold(spark, silver_path, gold_path):
    """
    Reads Silver layer data as batch Delta, adds purchase_month column,
    aggregates purchase metrics by store location and month, and writes
    results to Gold layer as batch Delta.
    
    Args:
        spark (SparkSession): Spark session object.
        silver_path (str): Path to Silver Delta table.
        gold_path (str): Output path for Gold Delta table.

    Returns:
        None
    """
    df = spark.read.format("delta").load(silver_path)
    df = add_purchase_month_column(df)
    df_agg = aggregate_purchase_metrics(df, ["store_location", "purchase_month"])
    df_agg.write.format("delta").mode("overwrite").save(gold_path)

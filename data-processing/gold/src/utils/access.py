from pyspark.sql import SparkSession

def grant_access_to_gold(spark: SparkSession, catalog: str, database: str):
    spark.sql(f"""
        GRANT ALL PRIVILEGES ON TABLE {catalog}.{database}.gold TO `data_engineers`
    """)

    spark.sql(f"""
        GRANT SELECT ON TABLE {catalog}.{database}.gold TO `data_scientists`
    """)

    spark.sql(f"""
        GRANT SELECT ON TABLE {catalog}.{database}.gold TO `data_analysts`
    """)

import logging
from pyspark.sql import SparkSession

logger = logging.getLogger(__name__)

def grant_access_to_gold(spark: SparkSession, catalog: str, database: str):
    """
    Grants permissions on the Gold table according to the governance policy:
    - ALL PRIVILEGES to data_engineers
    - SELECT to data_scientists
    - SELECT to data_analysts

    Args:
        spark (SparkSession): Spark session object.
        catalog (str): Databricks catalog name.
        database (str): Databricks schema (database) name.
    """
    try:
        gold_table = f"{catalog}.{database}.gold"

        logger.info(f"Granting ALL PRIVILEGES on table {gold_table} to the data_engineers group...")
        spark.sql(f"""
            GRANT ALL PRIVILEGES ON TABLE {gold_table} TO `data_engineers`
        """)

        logger.info(f"Granting SELECT on table {gold_table} to the data_scientists group...")
        spark.sql(f"""
            GRANT SELECT ON TABLE {gold_table} TO `data_scientists`
        """)

        logger.info(f"Granting SELECT on table {gold_table} to the data_analysts group...")
        spark.sql(f"""
            GRANT SELECT ON TABLE {gold_table} TO `data_analysts`
        """)

        logger.info(f"Permissions granted successfully on table {gold_table}")

    except Exception as e:
        logger.error(f"Error granting permissions on Gold table: {e}")
        raise

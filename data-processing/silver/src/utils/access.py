import logging

from pyspark.sql import SparkSession

logger = logging.getLogger(__name__)


def grant_access_to_silver(spark: SparkSession, catalog: str, database: str):
    """
    Grants permissions on the Silver table according to the governance policy:
    - ALL PRIVILEGES to data_engineers
    - SELECT to data_scientists
    - SELECT to data_analysts

    Args:
        spark (SparkSession): Spark session object.
        catalog (str): Databricks catalog name.
        database (str): Databricks schema (database) name.
    """
    try:
        silver_table = f"{catalog}.{database}.silver"

        logger.info(
            f"Granting ALL PRIVILEGES on table {silver_table} to the data_engineers group..."
        )
        spark.sql(f"""
            GRANT ALL PRIVILEGES ON TABLE {silver_table} TO `data_engineers`
        """)

        logger.info(
            f"Granting SELECT on table {silver_table} to the data_scientists group..."
        )
        spark.sql(f"""
            GRANT SELECT ON TABLE {silver_table} TO `data_scientists`
        """)

        logger.info(
            f"Granting SELECT on table {silver_table} to the data_analysts group..."
        )
        spark.sql(f"""
            GRANT SELECT ON TABLE {silver_table} TO `data_analysts`
        """)

        logger.info(f"Permissions granted successfully on table {silver_table}")

    except Exception as e:
        logger.error(f"Error granting permissions on Silver table: {e}")
        raise

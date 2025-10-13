import logging

from pyspark.sql import SparkSession

logger = logging.getLogger(__name__)


def grant_access_to_bronze(spark: SparkSession, catalog: str, database: str):
    """
    Grants permissions on the Bronze schema and catalog.

    Args:
        spark (SparkSession): Spark session object.
        catalog (str): Databricks catalog name.
        database (str): Databricks schema (database) name.
    """
    try:
        logger.info(f"Granting USE CATALOG permissions on {catalog}...")

        groups = ["data_engineers", "data_scientists", "data_analysts"]

        for group in groups:
            spark.sql(f"""
                GRANT USE CATALOG ON CATALOG {catalog} TO `{group}`
            """)

        bronze_schema = f"{catalog}.{database}.bronze"

        logger.info(
            f"Granting ALL PRIVILEGES permissions on "
            f"{bronze_schema} to data_engineers group..."
        )

        spark.sql(
            f"GRANT ALL PRIVILEGES ON TABLE {catalog}.{database}.bronze "
            f"TO `data_engineers`"
        )

        logger.info(f"Permissions granted successfully on {bronze_schema}")
    except Exception as e:
        logger.error(f"Error granting permissions on Bronze layer: {e}")
        raise

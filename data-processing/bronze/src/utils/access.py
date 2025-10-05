import logging
from pyspark.sql import SparkSession

logger = logging.getLogger(__name__)

def grant_access_to_bronze(spark: SparkSession, catalog: str, database: str):
    """
    Grants permissions on the Bronze schema/tables to the data engineers group.

    Args:
        spark (SparkSession): Spark session object.
        catalog (str): Databricks catalog name.
        database (str): Databricks schema (database) name.
    """
    try:
        bronze_schema = f"{catalog}.{database}.bronze"

        logger.info(f"Granting ALL PRIVILEGES permissions on {bronze_schema} to data_engineers group...")

        spark.sql(f"""
            GRANT ALL PRIVILEGES ON TABLE {catalog}.{database}.bronze TO `data_engineers`
        """)

        logger.info(f"Permissions granted successfully on {bronze_schema}")

    except Exception as e:
        logger.error(f"Error granting permissions on Bronze layer: {e}")
        raise

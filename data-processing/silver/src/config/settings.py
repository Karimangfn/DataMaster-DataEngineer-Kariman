"""
Dataset configuration for the Silver Layer data ingestion pipeline.
"""

import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    '--storage-account',
    required=True,
    help='Storage Account Name'
)
parser.add_argument(
    '--catalog',
    required=True,
    help='Databricks Catalog Name'
)
parser.add_argument(
    '--database',
    required=True,
    help='Databricks Database Name'
)
args = parser.parse_args()

storage_account = args.storage_account
catalog = args.catalog
database = args.database

DATASET_CONFIG = {
    "bronze_path": (
        f"abfss://bronze@{storage_account}.dfs.core.windows.net/"
        "customer_data/"
    ),
    "silver_path": (
        f"abfss://silver@{storage_account}.dfs.core.windows.net/"
        "customer_data/"
    ),
    "catalog": (
        catalog
    ),
    "database": (
        database
    )
}

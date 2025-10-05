"""
Dataset configuration for the Bronze Layer data ingestion pipeline.
"""

import argparse
import sys
import shlex

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
# args = parser.parse_args(shlex.split(" ".join(sys.argv[1:])))

storage_account = args.storage_account
catalog = args.catalog
database = args.database

DATASET_CONFIG = {
    "input_path": [
        f"abfss://raw@{storage_account}.dfs.core.windows.net/"
        "api/",
        f"abfss://raw@{storage_account}.dfs.core.windows.net/"
        "database/",
        f"abfss://raw@{storage_account}.dfs.core.windows.net/"
        "files/"
    ],
    "output_path": (
        f"abfss://bronze@{storage_account}.dfs.core.windows.net/"
        "customer_data/"
    ),
    "checkpoint_path": (
        f"abfss://bronze@{storage_account}.dfs.core.windows.net/"
        "checkpoints/"
    ),
    "catalog": (
        catalog
    ),
    "database": (
        database
    )
}

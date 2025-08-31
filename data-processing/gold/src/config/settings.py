"""
Dataset configuration for the Gold Layer data ingestion pipeline.
"""

import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    '--storage-account',
    required=True,
    help='Storage Account Name'
)
args = parser.parse_args()

storage_account = args.storage_account

DATASET_CONFIG = {
    "silver_path": (
        f"abfss://silver@{storage_account}.dfs.core.windows.net/"
        "customer_data/"
    ),
    "gold_path": (
        f"abfss://gold@{storage_account}.dfs.core.windows.net/"
        "customer_data/"
    )
}

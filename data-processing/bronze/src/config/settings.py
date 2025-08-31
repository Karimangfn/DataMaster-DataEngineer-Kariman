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
    )
}

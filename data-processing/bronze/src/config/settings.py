"""
Dataset configuration for the Bronze Layer data ingestion pipeline.
"""

DATASET_CONFIG = {
    "name": "customer_data",
    "input_path": (
        "abfss://raw@<storage>.dfs.core.windows.net/"
        "customer_data/"
    ),
    "output_path": (
        "abfss://bronze@<storage>.dfs.core.windows.net/"
        "customer_data/"
    ),
    "checkpoint_path": (
        "abfss://checkpoints@<storage>.dfs.core.windows.net/"
        "bronze/customer_data/"
    )
}

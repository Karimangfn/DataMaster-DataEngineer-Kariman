"""
Dataset configuration for the Silver Layer data ingestion pipeline.
"""

DATASET_CONFIG = {
    "bronze_path": (
        "abfss://bronze@<storage>.dfs.core.windows.net/"
        "customer_data/"
    ),
    "silver_path": (
        "abfss://silver@<storage>.dfs.core.windows.net/"
        "customer_data/"
    ),
    "silver_checkpoint_path": (
        "abfss://checkpoints@<storage>.dfs.core.windows.net/"
        "silver/customer_data/"
    )
}

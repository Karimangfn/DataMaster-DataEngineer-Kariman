"""
Dataset configuration for the Gold Layer data ingestion pipeline.
"""

DATASET_CONFIG = {
    "silver_path": (
        "abfss://silver@<storage>.dfs.core.windows.net/"
        "customer_data/"
    ),
    "gold_path": (
        "abfss://gold@<storage>.dfs.core.windows.net/"
        "customer_data/"
    ),
    "gold_checkpoint_path": (
        "abfss://checkpoints@<storage>.dfs.core.windows.net/"
        "gold/customer_data/"
    )
}

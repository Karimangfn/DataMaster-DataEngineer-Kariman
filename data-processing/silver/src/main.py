from config.settings import DATASET_CONFIG
from modules.silver_transform import transform_silver


def main():
    """
    Executes the Silver transformation pipeline.
    Reads streaming data from Bronze, processes it, and writes to Silver.
    """
    bronze_path = DATASET_CONFIG["bronze_path"]
    silver_path = DATASET_CONFIG["silver_path"]
    checkpoint_path = DATASET_CONFIG["silver_checkpoint_path"]

    transform_silver(spark, bronze_path, silver_path)


if __name__ == "__main__":
    main()

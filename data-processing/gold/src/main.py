from config.settings import DATASET_CONFIG
from modules.gold_transform import transform_gold


def main():
    """
    Executes the Gold transformation pipeline.
    Reads data from the Silver layer, aggregates purchases,
    and writes the results to the Gold layer as a streaming job.
    """
    silver_path = DATASET_CONFIG["silver_path"]
    gold_path = DATASET_CONFIG["gold_path"]
    checkpoint_path = DATASET_CONFIG["gold_checkpoint_path"]

    transform_gold(spark, silver_path, gold_path)


if __name__ == "__main__":
    main()

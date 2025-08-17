import logging
import os
import sys

base_dir = os.getcwd()

if base_dir not in sys.path:
    sys.path.insert(0, base_dir)

from config.settings import DATASET_CONFIG
from modules.gold_transform import transform_gold

logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def main():
    """
    Executes the Gold transformation pipeline.
    Reads data from the Silver layer, aggregates purchases,
    and writes the results to the Gold layer as a streaming job.
    """
    logger.info("Starting Gold pipeline execution")
    
    silver_path = DATASET_CONFIG["silver_path"]
    gold_path = DATASET_CONFIG["gold_path"]
    checkpoint_path = DATASET_CONFIG["gold_checkpoint_path"]

    transform_gold(spark, silver_path, gold_path)

    logger.info("Gold transformation pipeline completed successfully.")

if __name__ == "__main__":
    main()

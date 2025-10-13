import logging
import os
import sys

base_dir = os.getcwd()

if base_dir not in sys.path:
    sys.path.insert(0, base_dir)

from config.settings import DATASET_CONFIG
from modules.silver_transform import transform_silver

logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

logging.getLogger("py4j").setLevel(logging.ERROR)
logging.getLogger("py4j.clientserver").setLevel(logging.ERROR)


def main():
    """
    Executes the Silver transformation pipeline.
    Reads data from Bronze layer, processes it,
    and writes to Silver layer.
    """
    logger.info("Starting Silver pipeline execution")

    transform_silver(spark, DATASET_CONFIG)

    logging.info("Silver transformation pipeline completed successfully.")


if __name__ == "__main__":
    main()

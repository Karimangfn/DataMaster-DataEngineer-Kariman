import logging
import os
import sys

base_dir = os.getcwd()

if base_dir not in sys.path:
    sys.path.insert(0, base_dir)

from config.settings import DATASET_CONFIG
from modules.bronze_ingestion import ingest_bronze_customer_data
from modules.schemas import get_customer_schema
from utils.utils import detect_format_from_extension

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
    Executes the Bronze ingestion pipeline for customer data.
    Detects the file format, loads the schema, and starts the Auto Loader.
    """
    logger.info("Starting Bronze pipeline execution")

    logger.info(
        f"Checking files in input path: {DATASET_CONFIG['input_path']}"
    )

    for path in DATASET_CONFIG["input_path"]:
        try:
            raw_files = dbutils.fs.ls(path)
        except Exception as e:
            logger.warning(f"Could not list files in {path}: {e}")
            continue

        if not raw_files:
            logger.warning(f"No files found in {path}, skipping ingestion.")
            continue

        first_file = raw_files[0].name
        logger.info(f"First file found: {first_file}")

        file_format = detect_format_from_extension(first_file)
        logger.info(f"Detected file format: {file_format}")

        schema = get_customer_schema()
        logger.info("Schema loaded successfully")

        ingest_bronze_customer_data(
            spark,
            {**DATASET_CONFIG, "input_path": [path]},
            schema,
            file_format
        )
        logger.info("Bronze step executed successfully")


if __name__ == "__main__":
    main()

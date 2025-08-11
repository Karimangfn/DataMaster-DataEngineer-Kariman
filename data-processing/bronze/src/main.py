import logging
import sys
import os

try:
    base_dir = os.path.dirname(os.path.abspath(__file__))
except NameError:
    base_dir = os.getcwd()

print("base_dir:", base_dir)
print("listdir base_dir:", os.listdir(base_dir))

if base_dir not in sys.path:
    sys.path.insert(0, base_dir)

print("sys.path:", sys.path)

from config.settings import DATASET_CONFIG
from modules.bronze_ingestion import ingest_bronze_customer_data
from modules.schemas import get_customer_schema
from modules.utils import detect_format_from_extension

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    """
    Executes the Bronze ingestion pipeline for customer data.
    Detects the format of the dataset, loads the schema, and
    starts the Auto Loader process.
    """
    logger.info("Início da execução do pipeline Bronze")
    print("teste2")
    raw_files = dbutils.fs.ls(DATASET_CONFIG["input_path"])
    first_file = raw_files[0].name
    file_format = detect_format_from_extension(first_file)
    schema = get_customer_schema()
    ingest_bronze_customer_data(spark, DATASET_CONFIG, schema, file_format)

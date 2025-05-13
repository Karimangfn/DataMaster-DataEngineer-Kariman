import logging
import os

from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobClient
from strategy.ingestion_api import APIIngestion
from utils.utils import convert_to_json

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

logger = logging.getLogger(__name__)


def main():
    """
    Função principal que faz a ingestão de dados da API e grava no ADLS.
    """
    try:
        api_url = os.getenv("API_URL")
        api_key = os.getenv("API_KEY")

        storage_account = os.getenv("STORAGE_ACCOUNT")
        storage_container = os.getenv("STORAGE_CONTAINER")
        storage_folder = os.getenv("STORAGE_FOLDER")

        ingestion_service = APIIngestion(api_url, "rest")
        params = {"key": api_key}

        response = ingestion_service.ingest(params)
        data = convert_to_json(response)

        credential = DefaultAzureCredential()
        blob_name = f"{storage_folder}/data.json"

        blob_client = BlobClient(
            account_url=f"https://{storage_account}.blob.core.windows.net",
            container_name=storage_container,
            blob_name=blob_name,
            credential=credential,
        )

        blob_client.upload_blob(data, overwrite=True)

        logger.info(f"Ingestão realizada com sucesso para API: {api_url}")

    except Exception as e:
        logger.exception(f"Erro durante a execução: {e}")


if __name__ == "__main__":
    main()

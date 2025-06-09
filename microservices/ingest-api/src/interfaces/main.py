import os

from src.application.helpers.serialization import convert_to_json
from src.application.services.api_ingestion_service import APIIngestion
from src.domain.exceptions.exceptions import (APIIngestionError,
                                              AzureAuthenticationError,
                                              BlobUploadError,
                                              MissingEnvironmentVariableError)
from src.infrastructure.ingestion.rest_api_ingestion import RestAPIIngestion
from src.infrastructure.logging.logger import get_logger
from src.infrastructure.storage.azure_blob_uploader import AzureBlobUploader

logger = get_logger(__name__)


def main():
    """
    Main entry point that ingests data from an API
    and uploads it to Azure Blob Storage.
    """
    try:
        api_url = os.getenv("API_URL")
        api_key = os.getenv("API_KEY")
        storage_container = os.getenv("STORAGE_CONTAINER")
        storage_folder = os.getenv("STORAGE_FOLDER")

        if not all([api_url, api_key, storage_container, storage_folder]):
            raise MissingEnvironmentVariableError(
                [
                    var for var, value in {
                        "API_URL": api_url,
                        "API_KEY": api_key,
                        "STORAGE_CONTAINER": storage_container,
                        "STORAGE_FOLDER": storage_folder
                    }.items() if not value
                ]
            )

        strategy = RestAPIIngestion()
        ingestion_service = APIIngestion(api_url, strategy)
        response = ingestion_service.ingest(params={"key": api_key})
        data = convert_to_json(response)

        blob_uploader = AzureBlobUploader()
        blob_name = f"{storage_folder}/data.json"
        blob_uploader.upload_json(
            container_name=storage_container,
            blob_name=blob_name,
            json_content=data
        )

        logger.info(
            f"Data ingestion and upload completed successfully. "
            f"API: {api_url}, Blob: {blob_name}"
        )

    except (
        APIIngestionError,
        BlobUploadError,
        AzureAuthenticationError,
        MissingEnvironmentVariableError
    ) as e:
        logger.error(f"Ingestion process failed: {str(e)}")
    except Exception as e:
        logger.exception(f"Unexpected error during ingestion process: {e}")


if __name__ == "__main__":
    main()

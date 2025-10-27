import json
from datetime import datetime

from src.application.helpers.serialization import load_json
from src.application.services.api_ingestion_service import APIIngestionService
from src.application.validators.env_vars_validator import validate_env_vars
from src.domain.exceptions.exceptions import (APIIngestionError,
                                              AzureAuthenticationError,
                                              BlobUploadError,
                                              MissingEnvironmentVariableError,
                                              UnsupportedAPITypeError)
from src.infrastructure.config.strategy_registry import (AUTH_STRATEGIES,
                                                         INGESTION_STRATEGIES)
from src.infrastructure.logging.logging_setup import get_logger
from src.infrastructure.storage.azure_blob_uploader import AzureBlobUploader

logger = get_logger(__name__)


def main():
    """
    Main entry point that ingests data from an API
    and uploads it to Azure Blob Storage.
    new
    """
    try:
        required_vars = [
            "AUTH_TYPE",
            "API_TYPE",
            "API_URL",
            "API_KEY",
            "STORAGE_CONTAINER",
            "STORAGE_FOLDER",
        ]
        env_vars = validate_env_vars(required_vars)

        auth_type = env_vars["AUTH_TYPE"].lower()
        api_type = env_vars["API_TYPE"].lower()
        api_url = env_vars["API_URL"]
        api_key = env_vars["API_KEY"]
        storage_container = env_vars["STORAGE_CONTAINER"]
        storage_folder = env_vars["STORAGE_FOLDER"]

        logger.info(
            "Starting ingestion process",
            extra={
                "auth_type": auth_type,
                "api_type": api_type,
                "api_url": api_url,
                "storage_container": storage_container,
                "storage_folder": storage_folder,
            },
        )

        auth_cls = AUTH_STRATEGIES.get(auth_type)
        if not auth_cls:
            raise UnsupportedAPITypeError(
                f"Unsupported auth type: {auth_type}"
            )

        ingestion_cls = INGESTION_STRATEGIES.get(api_type)
        if not ingestion_cls:
            raise UnsupportedAPITypeError(
                f"Unsupported API type: {api_type}"
            )

        auth_strategy = auth_cls(api_key)
        ingestion_strategy = ingestion_cls(api_url, auth_strategy)
        ingestion_service = APIIngestionService(strategy=ingestion_strategy)

        response = ingestion_service.ingest()
        parsed_data = load_json(response)
        json_str = json.dumps(parsed_data)

        blob_uploader = AzureBlobUploader()
        blob_name = (
            f"{storage_folder}/data_"
            f"{datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')}.json"
        )
        blob_uploader.upload_json(
            container_name=storage_container,
            blob_name=blob_name,
            json_content=json_str
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
        print(f"Caught exception type: {type(e)} - {e}")
        logger.error(
            f"Ingestion process failed: {str(e)}"
        )
        raise
    except Exception as e:
        logger.error(
            f"Unexpected error during ingestion process: {e}"
        )
        raise

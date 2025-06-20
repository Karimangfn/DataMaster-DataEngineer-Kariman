import os

from azure.core.exceptions import AzureError
from azure.identity import ClientSecretCredential
from azure.storage.blob import BlobServiceClient
from src.domain.exceptions.exceptions import (AzureAuthenticationError,
                                              BlobUploadError,
                                              MissingEnvironmentVariableError)
from src.infrastructure.logging.logging_setup import get_logger

logger = get_logger(__name__)


class AzureBlobUploader:
    """
    Responsible for authenticating with Azure using Client Secret and
    uploading JSON files to Azure Blob Storage.
    """

    def __init__(self):
        """
        Initializes the upload service with credentials from environment
        variables.
        Raises MissingEnvironmentVariableError if any required variables
        are missing.
        """
        tenant_id = os.getenv("AZURE_TENANT_ID")
        client_id = os.getenv("AZURE_CLIENT_ID")
        client_secret = os.getenv("AZURE_CLIENT_SECRET")
        storage_account = os.getenv("STORAGE_ACCOUNT")

        missing_vars = [
            var_name for var_name, var in {
                "AZURE_TENANT_ID": tenant_id,
                "AZURE_CLIENT_ID": client_id,
                "AZURE_CLIENT_SECRET": client_secret,
                "STORAGE_ACCOUNT": storage_account,
            }.items() if not var
        ]

        if missing_vars:
            logger.error(
                f"Missing required environment variables: {missing_vars}"
            )
            raise MissingEnvironmentVariableError(missing_vars)

        try:
            self.credential = ClientSecretCredential(
                tenant_id, client_id, client_secret
            )
            self.blob_service_client = BlobServiceClient(
                f"https://{storage_account}.blob.core.windows.net",
                credential=self.credential,
            )
            logger.info(
                "AzureBlobUploader initialized successfully."
            )
        except AzureError as e:
            logger.error(
                "Failed to authenticate with BlobServiceClient."
            )
            raise AzureAuthenticationError(e)

    def upload_json(
        self, container_name: str, blob_name: str, json_content: str
    ) -> None:
        """
        Uploads a JSON string to Azure Blob Storage.

        Args:
            container_name (str): Name of the target container.
            blob_name (str): Name of the target blob.
            json_content (str): JSON content as a string.

        Raises:
            BlobUploadError: If an error occurs while uploading to Azure.
        """
        logger.debug(
            f"Starting upload of blob '{blob_name}' "
            f"to container '{container_name}'."
        )
        try:
            blob_client = self.blob_service_client.get_blob_client(
                container=container_name,
                blob=blob_name,
            )
            blob_client.upload_blob(json_content, overwrite=True)
            logger.info(
                f"Blob uploaded successfully: "
                f"{container_name}/{blob_name}"
            )
        except AzureError as e:
            logger.error(
                f"Failed to upload blob '{blob_name}' "
                f"to container '{container_name}'."
            )
            raise BlobUploadError(
                f"{container_name}/{blob_name}", e
            )

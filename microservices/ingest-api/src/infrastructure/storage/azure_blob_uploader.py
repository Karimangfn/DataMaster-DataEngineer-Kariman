import os
from typing import Dict

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

    def _get_env_vars(self) -> Dict[str, str]:
        """
        Retrieve and validate required environment variables for
        Azure authentication.

        Returns:
            Dict[str, str]: A dictionary containing the required
            environment variables.

        Raises:
            MissingEnvironmentVariableError: If any required
            environment variable is missing.
        """
        env_vars = {
            "AZURE_TENANT_ID": os.getenv("AZURE_TENANT_ID"),
            "AZURE_CLIENT_ID": os.getenv("AZURE_CLIENT_ID"),
            "AZURE_CLIENT_SECRET": os.getenv("AZURE_CLIENT_SECRET"),
            "STORAGE_ACCOUNT": os.getenv("STORAGE_ACCOUNT"),
        }
        missing_vars = [k for k, v in env_vars.items() if not v]
        if missing_vars:
            logger.error(
                f"Missing required environment variables: {missing_vars}"
            )
            raise MissingEnvironmentVariableError(missing_vars)
        return env_vars

    def __init__(self):
        """
        Initialize the AzureBlobUploader with credentials
        and BlobServiceClient.

        Retrieves required environment variables, authenticates using
        ClientSecretCredential, and initializes the BlobServiceClient.

        Raises:
            MissingEnvironmentVariableError: If any required environment
            variable is missing.
            AzureAuthenticationError: If authentication with Azure fails.
        """
        env_vars = self._get_env_vars()

        try:
            self.credential = ClientSecretCredential(
                env_vars["AZURE_TENANT_ID"],
                env_vars["AZURE_CLIENT_ID"],
                env_vars["AZURE_CLIENT_SECRET"],
            )
            self.blob_service_client = BlobServiceClient(
                f"https://{env_vars['STORAGE_ACCOUNT']}.blob.core.windows.net",
                credential=self.credential,
            )
            logger.info(
                "AzureBlobUploader initialized successfully."
            )
        except AzureError as e:
            logger.error(
                "Failed to authenticate with BlobServiceClient.",
                exc_info=True
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

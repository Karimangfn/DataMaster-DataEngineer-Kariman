import os
import tempfile
from unittest.mock import MagicMock, patch

import pytest
from src.domain.exceptions.exceptions import MissingEnvironmentVariableError
from src.infrastructure.storage.azure_blob_uploader import AzureBlobUploader


@pytest.fixture
def valid_env():
    """
    Provide valid environment variables for AzureBlobUploader.
    """
    valid_env_vars = {
        "AZURE_TENANT_ID": "tenant",
        "AZURE_CLIENT_ID": "client",
        "AZURE_CLIENT_SECRET": "secret",
        "STORAGE_ACCOUNT": "storageaccount",
    }
    with patch.dict(os.environ, valid_env_vars):
        yield


@patch(
    "src.infrastructure.storage.azure_blob_uploader."
    "ClientSecretCredential"
)
@patch("src.infrastructure.storage.azure_blob_uploader.BlobServiceClient")
def test_init_success(
    mock_blob_service_client,
    mock_credential,
    valid_env,
):
    """
    Verify AzureBlobUploader initializes correctly with
    valid environment variables.
    """
    mock_credential.return_value = "mock-credential"
    mock_blob_service_client.return_value = MagicMock()

    uploader = AzureBlobUploader()

    assert uploader.credential == "mock-credential"
    assert uploader.blob_service_client is not None


@patch.dict(os.environ, {}, clear=True)
def test_missing_env_vars():
    """
    Verify AzureBlobUploader raises MissingEnvironmentVariableError
    if required environment variables are missing.
    """
    with pytest.raises(MissingEnvironmentVariableError) as exc:
        AzureBlobUploader()
    missing_vars = [
        "AZURE_TENANT_ID",
        "AZURE_CLIENT_ID",
        "AZURE_CLIENT_SECRET",
        "STORAGE_ACCOUNT",
    ]
    for var in missing_vars:
        assert var in str(exc.value)


@patch(
    "src.infrastructure.storage.azure_blob_uploader."
    "ClientSecretCredential"
)
@patch("src.infrastructure.storage.azure_blob_uploader.BlobServiceClient")
def test_upload_file_success(
    mock_blob_service_client,
    mock_credential,
    valid_env,
):
    """
    Verify that upload_file successfully calls upload_blob
    on the Azure Blob client.
    """
    mock_credential.return_value = "credential"
    mock_blob_service_client_instance = MagicMock()
    mock_blob_service_client.return_value = mock_blob_service_client_instance

    mock_blob_client = MagicMock()
    mock_blob_service_client_instance.get_blob_client.return_value = (
        mock_blob_client
    )

    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as tmp:
        tmp.write('{"data": "value"}')
        tmp_path = tmp.name

    try:
        uploader = AzureBlobUploader()
        uploader.upload_file(
            "my-container",
            "path/file.json",
            tmp_path,
        )

        assert mock_blob_client.upload_blob.called
        args, kwargs = mock_blob_client.upload_blob.call_args
        assert kwargs["overwrite"] is True
    finally:
        os.remove(tmp_path)

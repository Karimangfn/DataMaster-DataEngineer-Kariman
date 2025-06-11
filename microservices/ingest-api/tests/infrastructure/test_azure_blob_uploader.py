import os
from unittest.mock import MagicMock, patch

import pytest
from src.domain.exceptions.exceptions import MissingEnvironmentVariableError
from src.infrastructure.storage.azure_blob_uploader import AzureBlobUploader


@pytest.fixture
def valid_env():
    """
    Fixture that sets required environment variables for AzureBlobUploader.
    Applies patch to os.environ with valid env vars during the test.
    """
    valid_env_vars = {
        "AZURE_TENANT_ID": "tenant",
        "AZURE_CLIENT_ID": "client",
        "AZURE_CLIENT_SECRET": "secret",
        "STORAGE_ACCOUNT": "storageaccount"
    }
    with patch.dict(os.environ, valid_env_vars):
        yield


@patch("src.infrastructure.storage.azure_blob_uploader.ClientSecretCredential")
@patch("src.infrastructure.storage.azure_blob_uploader.BlobServiceClient")
def test_init_success(
    mock_blob_service_client,
    mock_credential,
    valid_env
):
    """
    Test successful initialization of AzureBlobUploader when required
    environment variables are set.
    """
    mock_credential.return_value = "mock-credential"
    mock_blob_service_client.return_value = MagicMock()

    uploader = AzureBlobUploader()

    assert uploader.credential != "mock-credential"
    assert uploader.blob_service_client is not None


@patch.dict(os.environ, {}, clear=True)
def test_missing_env_vars():
    """
    Test that initialization raises MissingEnvironmentVariableError when
    required environment variables are missing.
    """
    with pytest.raises(MissingEnvironmentVariableError) as exc:
        AzureBlobUploader()
    assert "Missing required environment variables" in str(exc.value)


@patch("src.infrastructure.storage.azure_blob_uploader.ClientSecretCredential")
@patch("src.infrastructure.storage.azure_blob_uploader.BlobServiceClient")
def test_upload_json_success(
    mock_blob_service_client,
    mock_credential,
    valid_env
):
    """
    Test successful JSON upload to Azure Blob Storage.
    """
    mock_credential.return_value = "credential"
    mock_blob_service_client_instance = MagicMock()
    mock_blob_service_client.return_value = mock_blob_service_client_instance

    mock_blob_client = MagicMock()
    mock_blob_service_client_instance.get_blob_client.\
        return_value = mock_blob_client

    uploader = AzureBlobUploader()
    uploader.upload_json(
        "my-container",
        "path/file.json",
        '{"data": "value"}'
    )

    mock_blob_client.upload_blob.assert_called_once_with(
        '{"data": "value"}',
        overwrite=True
    )

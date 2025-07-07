import pytest
from src.domain.exceptions.exceptions import (AzureAuthenticationError,
                                              BlobUploadError, IngestionError,
                                              InvalidSourcePathError,
                                              MissingEnvironmentVariableError,
                                              NotFoundError,
                                              UnsupportedFileTypeError)


def test_ingestion_error():
    """
    Test that IngestionError can be raised and caught.
    """
    with pytest.raises(IngestionError):
        raise IngestionError("Ingestion base error")


def test_invalid_source_path_error():
    """
    Test that InvalidSourcePathError can be raised and caught.
    """
    with pytest.raises(InvalidSourcePathError):
        raise InvalidSourcePathError("Invalid source path")


def test_not_found_error():
    """
    Test that NotFoundError can be raised and caught.
    """
    with pytest.raises(NotFoundError):
        raise NotFoundError("Resource not found")


def test_unsupported_file_type_error():
    """
    Test that UnsupportedFileTypeError can be raised and caught.
    """
    with pytest.raises(UnsupportedFileTypeError):
        raise UnsupportedFileTypeError("Unsupported file type")


def test_azure_authentication_error():
    """
    Test that AzureAuthenticationError can be raised and caught.
    """
    with pytest.raises(AzureAuthenticationError):
        raise AzureAuthenticationError("Azure authentication failed")


def test_blob_upload_error():
    """
    Test that BlobUploadError can be raised and caught.
    """
    with pytest.raises(BlobUploadError):
        raise BlobUploadError("Upload failed")


def test_missing_environment_variable_error():
    """
    Test that MissingEnvironmentVariableError can be raised and caught.
    """
    with pytest.raises(MissingEnvironmentVariableError):
        raise MissingEnvironmentVariableError("Missing environment variables")

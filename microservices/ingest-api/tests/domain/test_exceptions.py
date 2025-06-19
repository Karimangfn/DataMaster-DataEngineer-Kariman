import pytest
from src.domain.exceptions.exceptions import (APIRequestError,
                                              AzureAuthenticationError,
                                              BlobUploadError,
                                              ConfigurationLoadError,
                                              IngestionError,
                                              JSONConversionError,
                                              MissingEnvironmentVariableError,
                                              UnsupportedAPITypeError)


def test_ingestion_error_base_class():
    """
    Tests that the IngestionError can be instantiated and that all
    specific exceptions correctly inherit from this base class.
    """
    with pytest.raises(IngestionError) as exc:
        raise IngestionError("General ingestion failure")
    assert "General ingestion failure" in str(exc.value)

    assert issubclass(APIRequestError, IngestionError)
    assert issubclass(JSONConversionError, IngestionError)
    assert issubclass(UnsupportedAPITypeError, IngestionError)
    assert issubclass(BlobUploadError, IngestionError)
    assert issubclass(MissingEnvironmentVariableError, IngestionError)
    assert issubclass(AzureAuthenticationError, IngestionError)


def test_unsupported_api_type_error():
    """
    Tests if UnsupportedAPITypeError returns the expected message.
    """
    with pytest.raises(UnsupportedAPITypeError) as exc:
        raise UnsupportedAPITypeError("SOAP")
    assert "API type 'SOAP' is not supported." in str(exc.value)


def test_api_request_error():
    """
    Tests if APIRequestError properly wraps an original exception.
    """
    try:
        raise ValueError("Connection error")
    except Exception as e:
        with pytest.raises(APIRequestError) as exc:
            raise APIRequestError("MyAPI", e)
        assert (
            "Failed to ingest data from API 'MyAPI': Connection error"
            in str(exc.value)
        )


def test_json_conversion_error():
    """
    Tests if JSONConversionError properly wraps the original exception.
    """
    try:
        raise TypeError("Invalid JSON")
    except Exception as e:
        with pytest.raises(JSONConversionError) as exc:
            raise JSONConversionError(e)
        assert (
            "Failed to convert response to JSON: Invalid JSON"
            in str(exc.value)
        )


def test_configuration_load_error():
    """
    Tests if ConfigurationLoadError correctly shows the config path
    and original error.
    """
    try:
        raise FileNotFoundError("File missing")
    except Exception as e:
        with pytest.raises(ConfigurationLoadError) as exc:
            raise ConfigurationLoadError("/path/config.json", e)
        assert (
            "Failed to load configuration from '/path/config.json': "
            "File missing" in str(exc.value)
        )


def test_blob_upload_error():
    """
    Tests if BlobUploadError correctly displays the destination
    and original exception.
    """
    try:
        raise IOError("Upload failed")
    except Exception as e:
        with pytest.raises(BlobUploadError) as exc:
            raise BlobUploadError("container/blob.txt", e)
        assert (
            "Failed to upload data to blob 'container/blob.txt': Upload failed"
            in str(exc.value)
        )


def test_missing_env_var_error():
    """
    Tests if MissingEnvironmentVariableError correctly
    lists the missing variables.
    """
    with pytest.raises(MissingEnvironmentVariableError) as exc:
        raise MissingEnvironmentVariableError(["API_KEY", "API_SECRET"])
    assert (
        "Missing required environment variables: API_KEY, API_SECRET"
        in str(exc.value)
    )


def test_azure_authentication_error():
    """
    Tests if AzureAuthenticationError properly wraps the original exception.
    """
    try:
        raise RuntimeError("Invalid credentials")
    except Exception as e:
        with pytest.raises(AzureAuthenticationError) as exc:
            raise AzureAuthenticationError(e)
        assert (
            "Failed to authenticate with Azure: Invalid credentials"
            in str(exc.value)
        )

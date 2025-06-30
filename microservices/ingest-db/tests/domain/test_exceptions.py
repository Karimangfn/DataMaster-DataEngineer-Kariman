import pytest
from src.domain.exceptions.exceptions import (AzureAuthenticationError,
                                              BlobUploadError,
                                              DatabaseIngestionError,
                                              IngestionError,
                                              MissingEnvironmentVariableError,
                                              UnsupportedDatabaseTypeError)


@pytest.mark.parametrize(
    "exception_cls",
    [
        DatabaseIngestionError,
        MissingEnvironmentVariableError,
        AzureAuthenticationError,
        BlobUploadError,
        UnsupportedDatabaseTypeError
    ]
)
def test_exception_is_subclass_of_ingestion_error(exception_cls):
    """
    Test that all custom exceptions are subclasses of IngestionError.
    """
    assert issubclass(exception_cls, IngestionError)


@pytest.mark.parametrize(
    "exception_cls, message",
    [
        (DatabaseIngestionError, "Database failed"),
        (MissingEnvironmentVariableError, "Missing VAR_X"),
        (AzureAuthenticationError, "Invalid token"),
        (BlobUploadError, "Upload failed"),
        (UnsupportedDatabaseTypeError, "Unsupported DB type")
    ]
)
def test_exception_instantiation_and_message(exception_cls, message):
    """
    Test that each exception can be instantiated with a message
    and retains it properly.
    """
    exception = exception_cls(message)
    assert str(exception) == message

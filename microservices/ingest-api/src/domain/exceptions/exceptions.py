class IngestionError(Exception):
    """Base class for ingestion-related errors."""
    pass


class UnsupportedAPITypeError(IngestionError):
    """Raised when an unsupported API type is provided."""
    def __init__(self, api_type: str):
        message = (
            f"API type '{api_type}' is not supported."
        )
        super().__init__(message)


class APIRequestError(IngestionError):
    """Raised when an API request fails."""
    def __init__(self, source: str, original_exception: Exception):
        message = (
            f"Failed to ingest data from API '{source}': "
            f"{str(original_exception)}"
        )
        super().__init__(message)


class APIIngestionError(IngestionError):
    """Raised when there is a general error during REST API ingestion."""
    def __init__(self, source: str, original_exception: Exception):
        message = (
            f"Failed to ingest data from API {source}: "
            f"{str(original_exception)}"
        )
        super().__init__(message)


class JSONConversionError(IngestionError):
    """Raised when the response from the API cannot be converted to JSON."""
    def __init__(self, original_exception: Exception):
        message = (
            f"Failed to convert response to JSON: "
            f"{str(original_exception)}"
        )
        super().__init__(message)


class ConfigurationLoadError(Exception):
    """Raised when configuration file loading fails."""
    def __init__(self, config_path: str, original_exception: Exception):
        message = (
            f"Failed to load configuration from '{config_path}': "
            f"{str(original_exception)}"
        )
        super().__init__(message)


class BlobUploadError(IngestionError):
    """Raised when the upload to Azure Blob Storage fails."""
    def __init__(self, destination: str, original_exception: Exception):
        message = (
            f"Failed to upload data to blob '{destination}': "
            f"{str(original_exception)}"
        )
        super().__init__(message)


class MissingEnvironmentVariableError(IngestionError):
    """Raised when required environment variables are missing."""
    def __init__(self, missing_vars: list[str]):
        joined_vars = ", ".join(missing_vars)
        message = (
            f"Missing required environment variables: {joined_vars}"
        )
        super().__init__(message)


class AzureAuthenticationError(IngestionError):
    """Raised when authentication with Azure fails."""
    def __init__(self, original_exception: Exception):
        message = (
            f"Failed to authenticate with Azure: "
            f"{str(original_exception)}"
        )
        super().__init__(message)

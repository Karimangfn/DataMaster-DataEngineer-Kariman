class ConfigurationLoadError(Exception):
    """Raised when configuration file loading fails."""
    pass


class IngestionError(Exception):
    """Base class for ingestion-related errors."""
    pass


class UnsupportedAPITypeError(IngestionError):
    """Raised when an unsupported API type is provided."""
    pass


class APIRequestError(IngestionError):
    """Raised when an API request fails."""
    pass


class APIIngestionError(IngestionError):
    """Raised when there is a general error during REST API ingestion."""
    pass


class JSONConversionError(IngestionError):
    """Raised when the response from the API cannot be converted to JSON."""
    pass


class BlobUploadError(IngestionError):
    """Raised when the upload to Azure Blob Storage fails."""
    pass


class MissingEnvironmentVariableError(IngestionError):
    """Raised when required environment variables are missing."""
    pass


class AzureAuthenticationError(IngestionError):
    """Raised when authentication with Azure fails."""
    pass

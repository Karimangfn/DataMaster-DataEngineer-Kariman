class IngestionError(Exception):
    """Base class for ingestion-related errors."""
    pass


class DatabaseIngestionError(IngestionError):
    """Raised when database ingestion fails."""
    pass


class MissingEnvironmentVariableError(IngestionError):
    """Raised when required environment variables are missing."""
    pass


class AzureAuthenticationError(IngestionError):
    """Raised when authentication with Azure fails."""
    pass


class BlobUploadError(IngestionError):
    """Raised when the upload to Azure Blob Storage fails."""
    pass


class UnsupportedDatabaseTypeError(IngestionError):
    """Raised when a database type or strategy is not supported."""
    pass

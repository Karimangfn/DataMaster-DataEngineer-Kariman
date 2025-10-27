class IngestionError(Exception):
    """Base class for ingestion-related errors.new"""
    pass


class InvalidSourcePathError(IngestionError):
    """Raised when the provided source path is missing"""
    pass


class NotFoundError(IngestionError):
    """Raised when expected resources are not found."""
    pass


class UnsupportedFileTypeError(IngestionError):
    """
    Raised when the detected file type is not supported by any
    ingestion strategy.
    """
    pass


class AzureAuthenticationError(IngestionError):
    """Raised when authentication with Azure fails."""
    pass


class BlobUploadError(IngestionError):
    """Raised when the upload to Azure Blob Storage fails."""
    pass


class MissingEnvironmentVariableError(IngestionError):
    """Raised when required environment variables are missing."""
    pass

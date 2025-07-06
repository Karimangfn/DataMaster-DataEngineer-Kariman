from src.application.helpers.config_loader import \
    load_ingestion_config_from_env
from src.application.services.files_ingestion_service import IngestionService
from src.domain.exceptions.exceptions import (BlobUploadError, IngestionError,
                                              InvalidSourcePathError,
                                              NotFoundError,
                                              UnsupportedFileTypeError)
from src.infrastructure.logging.logging_setup import get_logger

logger = get_logger(__name__)


def main():
    """
    Main entry point to execute the file ingestion process.

    Loads configuration, initializes the ingestion service,
    and executes the ingestion workflow.

    Raises:
        InvalidSourcePathError: If the source folder path is
        invalid or missing.
        NotFoundError: If no files are found in the source folder.
        UnsupportedFileTypeError: If the file type in the source
        folder is unsupported.
        BlobUploadError: If uploading a file to Azure Blob Storage fails.
        IngestionError: For other ingestion-related errors.
        Exception: For any other unexpected errors.
    """
    try:
        config = load_ingestion_config_from_env()
        service = IngestionService(config)
        service.execute()
        logger.info("File ingestion completed successfully.")
    except (
        InvalidSourcePathError,
        NotFoundError,
        UnsupportedFileTypeError,
    ) as e:
        logger.error(f"Configuration error: {e}")
    except BlobUploadError as e:
        logger.error(f"Blob upload failed: {e}")
    except IngestionError as e:
        logger.error(f"Ingestion process failed: {e}")
    except Exception as e:
        logger.exception(f"Critical unexpected error during execution: {e}")

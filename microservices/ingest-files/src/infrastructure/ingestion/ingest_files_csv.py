from src.domain.exceptions.exceptions import BlobUploadError
from src.domain.ports.ingestion_strategy import IngestionStrategy
from src.infrastructure.logging.logging_setup import get_logger
from src.infrastructure.storage.azure_blob_storage import AzureBlobUploader

logger = get_logger(__name__)


class IngestFilesCSV(IngestionStrategy):
    """
    Ingestion strategy for CSV files to Azure Blob Storage using
    AzureBlobUploader.
    """

    def __init__(self, config: dict):
        """
        Initialize the ingestion strategy with the required configuration.

        Args:
            config (dict): Configuration dictionary containing
                destination details.
        """
        self.config = config
        self.uploader = AzureBlobUploader()

        self.account_name = self.config[
            "destination"]["storage"]["raw"]["account"]
        self.container = self.config[
            "destination"]["storage"]["raw"]["container"]

        logger.info(
            f"IngestFilesCSV initialized for account: {self.account_name}, "
            f"container: {self.container}"
        )

    def ingest(self, source_path: str, destination_path: str) -> None:
        """
        Upload a CSV file from the local file system to Azure Blob Storage.

        Args:
            source_path (str): Local path to the source file.
            destination_path (str): Target path in Azure Blob Storage.

        Raises:
            BlobUploadError: If the upload to Azure Blob Storage fails.
        """
        logger.info(
            f"Starting upload of CSV file '{source_path}' to "
            f"'{destination_path}'"
        )
        try:
            self.uploader.upload_file(
                self.container,
                destination_path,
                source_path,
            )
            logger.info(
                f"Successfully uploaded CSV file '{source_path}' to "
                f"'{destination_path}'"
            )
        except BlobUploadError as e:
            logger.error(
                f"Failed to upload CSV file '{source_path}' to "
                f"'{destination_path}'",
                exc_info=True
            )
            raise BlobUploadError(
                f"Failed to upload CSV file {source_path} "
                f"to {destination_path}"
            ) from e

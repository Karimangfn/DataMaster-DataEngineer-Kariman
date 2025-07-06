from src.domain.exceptions.exceptions import BlobUploadError
from src.domain.ports.ingestion_strategy import IngestionStrategy
from src.infrastructure.storage.azure_blob_storage import AzureBlobUploader


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

    def ingest(self, source_path: str, destination_path: str) -> None:
        """
        Upload a CSV file from the local file system to Azure Blob Storage.

        Args:
            source_path (str): Local path to the source file.
            destination_path (str): Target path in Azure Blob Storage.

        Raises:
            BlobUploadError: If the upload to Azure Blob Storage fails.
        """
        try:
            self.uploader.upload_file(
                self.container,
                destination_path,
                source_path,
            )
        except BlobUploadError as e:
            raise BlobUploadError(
                f"Failed to upload CSV file {source_path} "
                f"to {destination_path}"
            ) from e

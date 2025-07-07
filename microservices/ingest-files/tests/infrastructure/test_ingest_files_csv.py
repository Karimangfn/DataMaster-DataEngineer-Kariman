from unittest.mock import MagicMock, patch

import pytest
from src.domain.exceptions.exceptions import BlobUploadError
from src.infrastructure.ingestion.ingest_files_csv import IngestFilesCSV


@pytest.fixture
def valid_config():
    """
    Provide a valid configuration dictionary for IngestFilesCSV.
    """
    return {
        "destination": {
            "storage": {
                "raw": {
                    "account": "mockaccount",
                    "container": "mockcontainer"
                }
            }
        }
    }


@pytest.fixture
def file_paths():
    """
    Provide common source and destination file paths for ingestion tests.
    """
    return ("source/file.csv", "container/file.csv")


@patch("src.infrastructure.ingestion.ingest_files_csv.AzureBlobUploader")
def test_ingest_success(mock_uploader_class, valid_config, file_paths):
    """
    Verify successful ingestion calls upload_file with correct parameters.
    """
    mock_uploader = MagicMock()
    mock_uploader_class.return_value = mock_uploader

    strategy = IngestFilesCSV(valid_config)
    source, destination = file_paths

    strategy.ingest(source, destination)

    mock_uploader.upload_file.assert_called_once_with(
        "mockcontainer", destination, source
    )


@patch("src.infrastructure.ingestion.ingest_files_csv.AzureBlobUploader")
def test_ingest_raises_blob_upload_error(
    mock_uploader_class,
    valid_config,
    file_paths
):
    """
    Verify ingestion raises BlobUploadError with expected
    message on upload failure.
    """
    mock_uploader = MagicMock()
    mock_uploader.upload_file.side_effect = BlobUploadError("Upload failed")
    mock_uploader_class.return_value = mock_uploader

    strategy = IngestFilesCSV(valid_config)
    source, destination = file_paths

    with pytest.raises(BlobUploadError, match="Failed to upload CSV file"):
        strategy.ingest(source, destination)

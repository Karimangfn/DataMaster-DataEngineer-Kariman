from unittest.mock import MagicMock, patch

import pytest
from src.application.services.files_ingestion_service import IngestionService
from src.domain.exceptions.exceptions import (InvalidSourcePathError,
                                              NotFoundError,
                                              UnsupportedFileTypeError)


@pytest.fixture
def valid_config(tmp_path):
    """
    Fixture that creates a temporary valid configuration
    with a test CSV file.
    """
    source_folder = tmp_path
    file = source_folder / "test.csv"
    file.write_text("id,name\n1,Alice")

    return {
        "source": {"folder": str(source_folder)},
        "destination": {
            "storage": {
                "raw": {
                    "account": "mockaccount",
                    "container": "mockcontainer",
                }
            }
        },
    }


@patch(
    "src.application.services.files_ingestion_service."
    "FILE_INGESTION_STRATEGIES",
    {"csv": MagicMock()},
)
def test_init_success(valid_config):
    """
    Test that the service initializes successfully with a valid configuration.
    """
    service = IngestionService(valid_config)
    assert service.source_path == valid_config["source"]["folder"]
    assert service.strategy is not None


def test_invalid_source_path_type():
    """
    Test that an invalid source path type raises InvalidSourcePathError.
    """
    config = {"source": {"folder": 123}}
    with pytest.raises(InvalidSourcePathError):
        IngestionService(config)


def test_nonexistent_source_path():
    """
    Test that a non-existent source path raises InvalidSourcePathError.
    """
    config = {"source": {"folder": "/path/does/not/exist"}}
    with pytest.raises(InvalidSourcePathError):
        IngestionService(config)


@patch("os.listdir", return_value=[])
@patch("os.path.isdir", return_value=True)
def test_no_files_found(mock_isdir, mock_listdir):
    """
    Test that NotFoundError is raised when no files are found in the directory.
    """
    config = {"source": {"folder": "/some/path"}}
    with patch("src.application.services.files_ingestion_service.logger"):
        with pytest.raises(NotFoundError):
            IngestionService(config)


@patch("os.listdir")
@patch("os.path.isfile", return_value=True)
@patch("os.path.isdir", return_value=True)
def test_unsupported_file_type(mock_isdir, mock_isfile, mock_listdir):
    """
    Test that UnsupportedFileTypeError is raised for unsupported file types.
    """
    mock_listdir.return_value = ["data.xyz"]
    config = {"source": {"folder": "/mock/path"}}
    with patch(
        "src.application.services.files_ingestion_service."
        "FILE_INGESTION_STRATEGIES",
        {},
    ):
        with patch("src.application.services.files_ingestion_service.logger"):
            with pytest.raises(UnsupportedFileTypeError):
                IngestionService(config)


@patch.dict(
    "src.application.services.files_ingestion_service."
    "FILE_INGESTION_STRATEGIES",
    {"csv": MagicMock()},
)
def test_execute_success(valid_config):
    """
    Test successful execution of the ingestion service.
    """
    mock_strategy_instance = MagicMock()
    mock_strategy_class = MagicMock(return_value=mock_strategy_instance)

    with patch.dict(
        "src.application.services.files_ingestion_service."
        "FILE_INGESTION_STRATEGIES",
        {"csv": mock_strategy_class},
    ):
        service = IngestionService(valid_config)
        service.execute()

        mock_strategy_instance.ingest.assert_called_once()

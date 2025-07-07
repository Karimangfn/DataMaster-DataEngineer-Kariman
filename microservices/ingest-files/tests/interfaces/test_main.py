from unittest import mock

import pytest
from src.domain.exceptions.exceptions import (BlobUploadError, IngestionError,
                                              InvalidSourcePathError,
                                              NotFoundError,
                                              UnsupportedFileTypeError)
from src.interfaces.main import main


@pytest.fixture
def mock_setup(monkeypatch):
    """
    Fixture to mock config loader and ingestion service,
    returning mocks for service class, config loader, and service instance.
    """
    mock_config_loader = mock.Mock()
    mock_config_loader.return_value = {"dummy": "config"}
    monkeypatch.setattr(
        "src.interfaces.main.load_ingestion_config_from_env",
        mock_config_loader
    )

    mock_service = mock.Mock()
    mock_service_class = mock.Mock(return_value=mock_service)
    monkeypatch.setattr(
        "src.interfaces.main.IngestionService", mock_service_class
    )

    return mock_service_class, mock_config_loader, mock_service


def test_main_success(mock_setup):
    """
    Verify that main() loads config, initializes the ingestion service,
    and executes ingestion successfully.
    """
    mock_service_class, mock_config_loader, mock_service = mock_setup

    main()

    mock_config_loader.assert_called_once()
    mock_service_class.assert_called_once_with({"dummy": "config"})
    mock_service.execute.assert_called_once()


@pytest.mark.parametrize(
    "exception",
    [
        InvalidSourcePathError("Invalid path"),
        NotFoundError("No files"),
        UnsupportedFileTypeError("Unsupported file"),
    ],
)
def test_main_config_errors(mock_setup, exception, caplog):
    """
    Verify that main() logs configuration-related errors
    when ingestion service raises certain exceptions.
    """
    mock_service_class, mock_config_loader, mock_service = mock_setup
    mock_service.execute.side_effect = exception

    main()

    assert any(
        "Configuration error" in msg for msg in caplog.text.splitlines()
    )


def test_main_blob_upload_error(mock_setup, caplog):
    """
    Verify that main() logs blob upload errors during ingestion.
    """
    mock_service_class, mock_config_loader, mock_service = mock_setup
    mock_service.execute.side_effect = BlobUploadError("Blob failed")

    main()

    assert "Blob upload failed" in caplog.text


def test_main_ingestion_error(mock_setup, caplog):
    """
    Verify that main() logs generic ingestion errors during ingestion.
    """
    mock_service_class, mock_config_loader, mock_service = mock_setup
    mock_service.execute.side_effect = IngestionError("Failed")

    main()

    assert "Ingestion process failed" in caplog.text


def test_main_generic_exception(mock_setup, caplog):
    """
    Verify that main() logs critical unexpected errors during execution.
    """
    mock_service_class, mock_config_loader, mock_service = mock_setup
    mock_service.execute.side_effect = Exception("Unexpected error")

    main()

    assert "Critical unexpected error during execution" in caplog.text

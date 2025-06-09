from unittest.mock import MagicMock, patch

import pytest
from src.domain.exceptions.exceptions import (APIIngestionError,
                                              AzureAuthenticationError,
                                              BlobUploadError)
from src.interfaces import main


@pytest.fixture
def env_vars():
    return {
        "API_URL": "http://fakeapi.com",
        "API_KEY": "fakekey",
        "STORAGE_CONTAINER": "container",
        "STORAGE_FOLDER": "folder",
    }


@pytest.fixture
def setup_mocks():
    with patch(
             'src.interfaces.main.logger'
         ) as mock_logger, \
         patch(
             'src.interfaces.main.RestAPIIngestion'
         ) as mock_strategy_class, \
         patch(
             'src.interfaces.main.APIIngestion'
         ) as mock_ingestion_class, \
         patch(
             'src.interfaces.main.AzureBlobUploader'
         ) as mock_blob_class, \
         patch(
             'src.interfaces.main.convert_to_json'
         ) as mock_convert:

        mock_strategy = MagicMock()
        mock_strategy_class.return_value = mock_strategy

        mock_ingestion = MagicMock()
        mock_ingestion_class.return_value = mock_ingestion

        mock_blob = MagicMock()
        mock_blob_class.return_value = mock_blob

        mock_convert.return_value = '{"some":"json"}'
        mock_ingestion.ingest.return_value = {"some": "response"}

        yield {
            "logger": mock_logger,
            "strategy_class": mock_strategy_class,
            "strategy": mock_strategy,
            "ingestion_class": mock_ingestion_class,
            "ingestion": mock_ingestion,
            "blob_class": mock_blob_class,
            "blob": mock_blob,
            "convert": mock_convert,
        }


@pytest.mark.parametrize("env", [
    {
        "API_URL": "http://fakeapi.com",
        "API_KEY": "fakekey",
        "STORAGE_CONTAINER": "container",
        "STORAGE_FOLDER": "folder",
    }
])
def test_main_success(env, setup_mocks):
    """
    Test successful data ingestion and upload flow.
    """
    with patch.dict('os.environ', env):
        main.main()

    setup_mocks["strategy_class"].assert_called_once()
    setup_mocks["ingestion_class"].assert_called_once_with(
        env["API_URL"], setup_mocks["strategy"]
    )
    setup_mocks["ingestion"].ingest.assert_called_once_with(
        params={"key": env["API_KEY"]}
    )
    setup_mocks["convert"].assert_called_once_with({"some": "response"})
    setup_mocks["blob"].upload_json.assert_called_once_with(
        container_name=env["STORAGE_CONTAINER"],
        blob_name=f"{env['STORAGE_FOLDER']}/data.json",
        json_content='{"some":"json"}'
    )
    setup_mocks["logger"].info.assert_called()


def test_missing_environment_variables(setup_mocks):
    """
    Test that MissingEnvironmentVariableError is raised
    and logged when env vars are missing.
    """
    with patch.dict('os.environ', {}, clear=True):
        main.main()

    setup_mocks["logger"].error.assert_called()
    setup_mocks["blob"].upload_json.assert_not_called()


def test_api_ingestion_error_handling(env_vars, setup_mocks):
    """
    Test handling of APIIngestionError during ingestion.
    """
    with patch.dict('os.environ', env_vars):
        setup_mocks["ingestion"].ingest.side_effect = APIIngestionError(
            source=env_vars["API_URL"],
            original_exception=Exception("API error")
        )
        main.main()

    setup_mocks["logger"].error.assert_called()
    setup_mocks["blob"].upload_json.assert_not_called()


def test_blob_upload_error_handling(env_vars, setup_mocks):
    """
    Test handling of BlobUploadError during upload.
    """
    with patch.dict('os.environ', env_vars):
        setup_mocks["blob"].upload_json.side_effect = BlobUploadError(
            destination=(
                f"{env_vars['STORAGE_CONTAINER']}/"
                f"{env_vars['STORAGE_FOLDER']}/data.json"
            ),
            original_exception=Exception("Blob error")
        )
        main.main()

    setup_mocks["logger"].error.assert_called()


def test_azure_authentication_error_handling(env_vars, setup_mocks):
    """
    Test handling of AzureAuthenticationError during ingestion or upload.
    """
    with patch.dict('os.environ', env_vars):
        setup_mocks["ingestion"].ingest.side_effect = AzureAuthenticationError(
            original_exception=Exception("Auth error")
        )
        main.main()

    setup_mocks["logger"].error.assert_called()


def test_unexpected_exception_handling(env_vars, setup_mocks):
    """
    Test that unexpected exceptions are logged with exception level.
    """
    with patch.dict('os.environ', env_vars):
        setup_mocks["ingestion"].ingest.side_effect = Exception("Unexpected")

        main.main()

    setup_mocks["logger"].exception.assert_called()

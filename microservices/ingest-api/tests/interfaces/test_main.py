from unittest.mock import MagicMock, patch

import pytest
from src.domain.exceptions.exceptions import UnsupportedAPITypeError
from src.interfaces.main import main


@pytest.fixture
def valid_env_vars():
    """
    Provide a valid environment variables dict.
    """
    return {
        "AUTH_TYPE": "basic",
        "API_TYPE": "rest",
        "API_URL": "http://example.com/api",
        "API_KEY": "secret",
        "STORAGE_CONTAINER": "container",
        "STORAGE_FOLDER": "folder",
    }


@pytest.fixture
def patch_all_dependencies(valid_env_vars):
    """
    Patch external dependencies inside src.interfaces.main for test isolation.
    """
    with patch(
        "src.interfaces.main.validate_env_vars", return_value=valid_env_vars
    ), patch(
        "src.interfaces.main.AUTH_STRATEGIES",
        {"basic": lambda key: MagicMock()},
    ), patch(
        "src.interfaces.main.INGESTION_STRATEGIES",
        {"rest": lambda url, auth: MagicMock()},
    ), patch(
        "src.interfaces.main.APIIngestionService"
    ) as MockAPIIngestionService, patch(
        "src.interfaces.main.convert_to_json",
        side_effect=lambda x: '{"mocked":"json"}',
    ), patch(
        "src.interfaces.main.AzureBlobUploader"
    ) as MockUploader, patch(
        "src.interfaces.main.logger", new=MagicMock()
    ) as mock_logger:

        mock_ingestion_instance = MockAPIIngestionService.return_value
        mock_ingestion_instance.ingest.return_value = {"some": "response"}

        mock_uploader_instance = MockUploader.return_value

        mock_logger_instance = mock_logger

        yield {
            "MockAPIIngestionService": MockAPIIngestionService,
            "mock_ingestion_instance": mock_ingestion_instance,
            "mock_uploader_instance": mock_uploader_instance,
            "mock_logger_instance": mock_logger_instance,
        }


def test_main_success(patch_all_dependencies):
    """
    Test main() runs successfully and uploads data as expected.
    """
    main()

    patch_all_dependencies["mock_logger_instance"].info.assert_any_call(
        "Starting ingestion process",
        extra={
            "auth_type": "basic",
            "api_type": "rest",
            "api_url": "http://example.com/api",
            "storage_container": "container",
            "storage_folder": "folder",
        }
    )
    patch_all_dependencies["MockAPIIngestionService"].assert_called_once()
    patch_all_dependencies["mock_ingestion_instance"] \
        .ingest.assert_called_once()
    patch_all_dependencies["mock_uploader_instance"] \
        .upload_json.assert_called_once_with(
        container_name="container",
        blob_name="folder/data.json",
        json_content='{"mocked":"json"}'
    )
    patch_all_dependencies["mock_logger_instance"].info.assert_any_call(
        "Data ingestion and upload completed successfully. "
        "API: http://example.com/api, Blob: folder/data.json"
    )


def test_main_unsupported_auth_type_raises(valid_env_vars):
    """
    Test main() raises UnsupportedAPITypeError for unsupported auth type.
    """
    invalid_env_vars = valid_env_vars.copy()
    invalid_env_vars["AUTH_TYPE"] = "unsupported_auth"

    with patch("src.interfaces.main.validate_env_vars",
               return_value=invalid_env_vars), \
         patch("src.interfaces.main.AUTH_STRATEGIES", {}), \
         patch("src.interfaces.main.INGESTION_STRATEGIES",
               {"rest": lambda url, auth: MagicMock()}):
        with pytest.raises(UnsupportedAPITypeError):
            main()


def test_main_unsupported_api_type_raises(valid_env_vars):
    """
    Test main() raises UnsupportedAPITypeError for unsupported API type.
    """
    invalid_env_vars = valid_env_vars.copy()
    invalid_env_vars["API_TYPE"] = "unsupported_api"

    with patch("src.interfaces.main.validate_env_vars",
               return_value=invalid_env_vars), \
         patch("src.interfaces.main.AUTH_STRATEGIES",
               {"basic": lambda key: MagicMock()}), \
         patch("src.interfaces.main.INGESTION_STRATEGIES", {}):
        with pytest.raises(UnsupportedAPITypeError):
            main()

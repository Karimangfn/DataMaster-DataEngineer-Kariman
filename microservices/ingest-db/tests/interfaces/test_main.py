from unittest import mock
from unittest.mock import MagicMock, patch

import pytest
from src.domain.exceptions.exceptions import MissingEnvironmentVariableError
from src.interfaces.main import main


@pytest.fixture
def env_vars():
    """
    Provide a valid set of environment variables with a valid DSN format.
    """
    return {
        "DB_TYPE": "postgres",
        "DB_CONN_STRING": "user=foo password=bar host=localhost dbname=test",
        "DB_QUERY": "SELECT 1",
        "STORAGE_CONTAINER": "container",
        "STORAGE_FOLDER": "folder",
        "STORAGE_ACCOUNT": "account",
        "AZURE_TENANT_ID": "tenant",
        "AZURE_CLIENT_ID": "client",
        "AZURE_CLIENT_SECRET": "secret",
    }


@pytest.fixture
def mock_strategies():
    """
    Provide mocks for connection and ingestion strategy
    classes and instances.
    """
    mock_conn_cls = MagicMock()
    mock_ingestion_cls = MagicMock()
    mock_conn_instance = MagicMock()
    mock_ingestion_instance = MagicMock()
    mock_conn_cls.return_value = mock_conn_instance
    mock_ingestion_cls.return_value = mock_ingestion_instance
    return mock_conn_cls, mock_ingestion_cls, mock_ingestion_instance


@pytest.fixture
def patch_service():
    """
    Patch DatabaseIngestionService class.
    """
    with patch(
        "src.interfaces.main.DatabaseIngestionService"
    ) as mock_service_cls:
        yield mock_service_cls


@pytest.fixture
def patch_blob_uploader():
    with patch("src.interfaces.main.AzureBlobUploader") as mock_cls:
        mock_instance = MagicMock()
        mock_cls.return_value = mock_instance
        yield mock_cls, mock_instance


@pytest.fixture
def patch_validate_env_vars(env_vars):
    """
    Patch environment variables validator to return valid env vars.
    """
    with patch(
        "src.interfaces.main.validate_env_vars"
    ) as mock_validate_env_vars:
        mock_validate_env_vars.return_value = env_vars
        yield mock_validate_env_vars


@pytest.fixture
def patch_strategy_registries(mock_strategies):
    """
    Patch connection and ingestion strategy registries with mocks.
    """
    mock_conn_cls, mock_ingestion_cls, _ = mock_strategies
    with mock.patch.dict(
        "src.infrastructure.config.strategy_registry.CONNECTION_STRATEGIES",
        {"postgres": mock_conn_cls},
    ), mock.patch.dict(
        "src.infrastructure.config.strategy_registry.INGESTION_STRATEGIES",
        {"postgres": mock_ingestion_cls},
    ):
        yield mock_conn_cls, mock_ingestion_cls


def test_main_success(
    patch_validate_env_vars,
    patch_strategy_registries,
    patch_service,
    patch_blob_uploader,
):
    """
    Test main function success path with valid inputs and strategies.
    """
    mock_blob_cls, mock_blob_instance = patch_blob_uploader
    mock_conn_cls, mock_ingestion_cls = patch_strategy_registries
    mock_service_cls = patch_service

    mock_service_instance = MagicMock()
    mock_service_instance.ingest.return_value = [{"result": 123}]
    mock_service_cls.return_value = mock_service_instance

    main()

    patch_validate_env_vars.assert_called_once_with(
        [
            "DB_TYPE", "DB_CONN_STRING", "DB_QUERY",
            "STORAGE_CONTAINER", "STORAGE_FOLDER"
        ]
    )

    mock_conn_cls.assert_called_once_with(
        "user=foo password=bar host=localhost dbname=test"
    )
    mock_ingestion_cls.assert_called_once_with(
        mock_conn_cls.return_value,
        "SELECT 1",
    )
    mock_service_cls.assert_called_once_with(mock_ingestion_cls.return_value)
    mock_service_instance.ingest.assert_called_once()


@patch(
    "src.interfaces.main.validate_env_vars",
    side_effect=MissingEnvironmentVariableError("Missing vars"),
)
def test_main_missing_env_vars(mock_validate_env_vars):
    """
    Test main function raises MissingEnvironmentVariableError
    when env vars missing.
    """
    with pytest.raises(MissingEnvironmentVariableError):
        main()


@patch("src.interfaces.main.validate_env_vars")
def test_main_unsupported_db_type(mock_validate_env_vars):
    """
    Test main function raises ValueError for unsupported database type.
    """
    mock_validate_env_vars.return_value = {
        "DB_TYPE": "unsupported_db",
        "DB_CONN_STRING": "user=foo password=bar host=localhost dbname=test",
        "DB_QUERY": "query",
        "STORAGE_CONTAINER": "container",
        "STORAGE_FOLDER": "folder",
    }
    with pytest.raises(ValueError):
        main()


@patch("src.interfaces.main.DatabaseIngestionService")
@patch("src.interfaces.main.validate_env_vars")
def test_main_unexpected_error(mock_validate_env_vars, mock_service_cls):
    """
    Test main function raises Exception on unexpected
    error during ingestion.
    """
    mock_validate_env_vars.return_value = {
        "DB_TYPE": "postgres",
        "DB_CONN_STRING": "user=foo password=bar host=localhost dbname=test",
        "DB_QUERY": "query",
        "STORAGE_CONTAINER": "container",
        "STORAGE_FOLDER": "folder",
    }

    mock_conn_cls = MagicMock()
    mock_ingestion_cls = MagicMock()

    with mock.patch.dict(
        "src.infrastructure.config.strategy_registry.CONNECTION_STRATEGIES",
        {"postgres": mock_conn_cls},
    ), mock.patch.dict(
        "src.infrastructure.config.strategy_registry.INGESTION_STRATEGIES",
        {"postgres": mock_ingestion_cls},
    ):

        mock_service_instance = MagicMock()
        mock_service_instance.ingest.side_effect = Exception(
            "Unexpected failure"
        )
        mock_service_cls.return_value = mock_service_instance

        with pytest.raises(Exception, match="Unexpected failure"):
            main()

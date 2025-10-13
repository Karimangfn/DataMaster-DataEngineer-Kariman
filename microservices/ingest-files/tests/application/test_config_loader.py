from unittest.mock import patch

from src.application.helpers.config_loader import \
    load_ingestion_config_from_env


@patch("src.application.helpers.config_loader.validate_env_vars")
def test_load_ingestion_config_from_env(mock_validate_env_vars):
    """
    Test loading the ingestion configuration from environment variables.
    """
    mock_validate_env_vars.return_value = {
        "AZURE_TENANT_ID": "tenant-id",
        "AZURE_CLIENT_ID": "client-id",
        "AZURE_CLIENT_SECRET": "client-secret",
        "STORAGE_ACCOUNT": "account-name",
        "STORAGE_CONTAINER": "container-name",
        "SOURCE_FOLDER": "/some/source/folder",
        "STORAGE_FOLDER": "raw-folder",
    }

    config = load_ingestion_config_from_env()

    assert config["azure"]["tenantId"] == "tenant-id"
    assert config["azure"]["clientId"] == "client-id"
    assert config["azure"]["clientSecret"] == "client-secret"
    assert config[
        "destination"]["storage"]["raw"]["account"] == "account-name"
    assert config[
        "destination"]["storage"]["raw"]["container"] == "container-name"
    assert config["source"]["folder"] == "/some/source/folder"
    mock_validate_env_vars.assert_called_once()

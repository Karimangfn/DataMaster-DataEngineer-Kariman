from src.application.validators.env_vars_validator import validate_env_vars


def load_ingestion_config_from_env() -> dict:
    """
    Load and structure ingestion configuration from environment variables.

    Returns:
        dict: Structured config dict for ingestion process.
    """
    required_vars = [
        "AZURE_TENANT_ID",
        "AZURE_CLIENT_ID",
        "AZURE_CLIENT_SECRET",
        "STORAGE_ACCOUNT",
        "STORAGE_CONTAINER",
        "SOURCE_FOLDER",
    ]

    env = validate_env_vars(required_vars)

    return {
        "azure": {
            "tenantId": env["AZURE_TENANT_ID"],
            "clientId": env["AZURE_CLIENT_ID"],
            "clientSecret": env["AZURE_CLIENT_SECRET"],
        },
        "destination": {
            "storage": {
                "raw": {
                    "account": env["STORAGE_ACCOUNT"],
                    "container": env["STORAGE_CONTAINER"],
                }
            }
        },
        "source": {
            "folder": env["SOURCE_FOLDER"],
        }
    }

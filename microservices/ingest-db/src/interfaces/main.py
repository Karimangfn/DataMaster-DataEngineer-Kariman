import json
from datetime import datetime

from src.application.services.database_ingestion_service import \
    DatabaseIngestionService
from src.application.validators.env_vars_validator import validate_env_vars
from src.domain.exceptions.exceptions import (IngestionError,
                                              MissingEnvironmentVariableError,
                                              UnsupportedDatabaseTypeError)
from src.infrastructure.config.strategy_registry import (CONNECTION_STRATEGIES,
                                                         INGESTION_STRATEGIES)
from src.infrastructure.logging.logging_setup import get_logger
from src.infrastructure.storage.azure_blob_uploader import AzureBlobUploader

logger = get_logger(__name__)


def main():
    """
    Main entry point that ingests data from a database
    using specified connection and query, then outputs the result.
    new
    """
    try:
        required_vars = [
            "DB_TYPE",
            "DB_CONN_STRING",
            "DB_QUERY",
            "STORAGE_CONTAINER",
            "STORAGE_FOLDER"
        ]
        env_vars = validate_env_vars(required_vars)

        db_type = env_vars["DB_TYPE"].lower()
        conn_string = env_vars["DB_CONN_STRING"]
        query = env_vars["DB_QUERY"]
        storage_container = env_vars["STORAGE_CONTAINER"]
        storage_folder = env_vars["STORAGE_FOLDER"]

        logger.info(f"Starting database ingestion for DB_TYPE={db_type}")

        connection_cls = CONNECTION_STRATEGIES.get(db_type)
        ingestion_cls = INGESTION_STRATEGIES.get(db_type)

        if not connection_cls or not ingestion_cls:
            raise ValueError(
                f"Unsupported strategy for DB_TYPE: {db_type}"
            )

        conn_strategy = connection_cls(conn_string)
        ingestion_strategy = ingestion_cls(conn_strategy, query)

        service = DatabaseIngestionService(ingestion_strategy)
        data = service.ingest()

        json_str = json.dumps(data, default=str)

        blob_uploader = AzureBlobUploader()
        blob_name = (
            f"{storage_folder}/data_"
            f"{datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')}.json"
        )
        blob_uploader.upload_json(
            container_name=storage_container,
            blob_name=blob_name,
            json_content=json_str
        )

        logger.info(
            "Database ingestion completed successfully."
        )
    except (
        IngestionError,
        MissingEnvironmentVariableError,
        UnsupportedDatabaseTypeError
    ) as e:
        logger.error(
            f"Ingestion process failed: {str(e)}",
            exc_info=True
        )
        raise
    except Exception as e:
        logger.error(
            f"Unexpected error during database ingestion: {str(e)}",
            exc_info=True
        )
        raise

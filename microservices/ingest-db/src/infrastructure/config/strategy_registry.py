from typing import Dict, Type

from src.domain.ports.connection_strategy import DatabaseConnectionStrategy
from src.domain.ports.ingestion_strategy import DatabaseIngestionStrategy
from src.infrastructure.connection.postgres_connection import \
    PostgresConnection
from src.infrastructure.ingestion.postgres_ingestion import PostgresIngestion

# Mapping of supported database connection strategies by type name
CONNECTION_STRATEGIES: Dict[str, Type[DatabaseConnectionStrategy]] = {
    "postgresql": PostgresConnection
}

# Mapping of supported database ingestion strategies by type name
INGESTION_STRATEGIES: Dict[str, Type[DatabaseIngestionStrategy]] = {
    "postgresql": PostgresIngestion
}

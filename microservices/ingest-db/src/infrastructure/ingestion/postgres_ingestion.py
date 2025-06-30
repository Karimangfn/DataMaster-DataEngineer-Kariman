from typing import Any

from src.domain.ports.connection_strategy import DatabaseConnectionStrategy
from src.domain.ports.ingestion_strategy import DatabaseIngestionStrategy
from src.infrastructure.logging.logging_setup import get_logger

logger = get_logger(__name__)


class PostgresIngestion(DatabaseIngestionStrategy):
    """Ingests data from a PostgreSQL database using a provided SQL query."""

    def __init__(self, conn_strategy: DatabaseConnectionStrategy, query: str):
        """
        Initialize with a connection strategy and SQL query.

        Args:
            conn_strategy (DatabaseConnectionStrategy): Strategy to create
            a database connection.
            query (str): SQL query to execute.
        """
        self._conn_strategy = conn_strategy
        self._query = query

    def ingest(self) -> Any:
        """
        Execute the SQL query and return the result.

        Returns:
            Any: The result of the SQL query.

        Raises:
            Exception: If query execution or connection fails.
        """
        conn = self._conn_strategy.get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute(self._query)
                result = cursor.fetchall()
                logger.info("Query executed successfully.")
                return result
        finally:
            conn.close()

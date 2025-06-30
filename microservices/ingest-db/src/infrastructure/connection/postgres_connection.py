import psycopg2
from psycopg2.extras import RealDictCursor
from src.domain.ports.connection_strategy import DatabaseConnectionStrategy
from src.infrastructure.logging.logging_setup import get_logger

logger = get_logger(__name__)


class PostgresConnection(DatabaseConnectionStrategy):
    """
    Database connection strategy for PostgreSQL using psycopg2.
    """

    def __init__(self, conn_str: str):
        """
        Initialize the PostgreSQL connection with the given connection string.

        Args:
            conn_str (str): Connection string used to connect to PostgreSQL.
        """
        self._conn_str = conn_str

    def get_connection(self):
        """
        Establish and return a connection to the PostgreSQL database.

        Returns:
            connection: psycopg2 connection object.

        Raises:
            Exception: If the connection attempt fails.
        """
        try:
            conn = psycopg2.connect(
                self._conn_str,
                cursor_factory=RealDictCursor
            )
            logger.info(
                "PostgreSQL connection established successfully."
            )
            return conn
        except Exception as e:
            logger.error(
                "Failed to connect to PostgreSQL.",
                exc_info=True
            )
            raise e

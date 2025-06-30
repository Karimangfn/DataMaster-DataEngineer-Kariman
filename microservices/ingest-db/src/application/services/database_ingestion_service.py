from typing import Any

from src.domain.exceptions.exceptions import IngestionError
from src.domain.ports.ingestion_strategy import DatabaseIngestionStrategy
from src.infrastructure.logging.logging_setup import get_logger

logger = get_logger(__name__)


class DatabaseIngestion:
    """Context class for database ingestion, using strategy pattern."""

    def __init__(self, strategy: DatabaseIngestionStrategy):
        """
        Initialize the DatabaseIngestion context.

        Args:
            strategy (DatabaseIngestionStrategy): A concrete ingestion
            strategy implementation.
        """
        self._strategy = strategy

    def ingest(self) -> Any:
        """
        Execute the ingestion using the configured strategy.

        Returns:
            Any: The raw result retrieved from the database.

        Raises:
            IngestionError: If the ingestion strategy raises an error.
        """
        logger.info(
            f"Starting database ingestion using strategy: "
            f"{type(self._strategy).__name__}"
        )
        try:
            result = self._strategy.ingest()
            logger.info(
                "Database ingestion completed successfully."
            )
            return result
        except Exception as e:
            logger.error(
                f"Failed to ingest using strategy "
                f"{type(self._strategy).__name__}: "
                f"{e}", exc_info=True
            )
            raise IngestionError(str(e))

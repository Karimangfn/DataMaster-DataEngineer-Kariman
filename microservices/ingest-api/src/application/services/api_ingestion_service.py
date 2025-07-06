from typing import Any

from src.domain.exceptions.exceptions import APIRequestError
from src.domain.ports.ingestion_strategy import APIIngestionStrategy
from src.infrastructure.logging.logging_setup import get_logger

logger = get_logger(__name__)


class APIIngestionService:
    """Context class for API ingestion, using strategy pattern."""

    def __init__(self, strategy: APIIngestionStrategy):
        """
        Initialize the APIIngestion context.

        Args:
            strategy (APIIngestionStrategy): A concrete ingestion
            strategy implementation.
        """
        self._strategy = strategy

    def ingest(self) -> Any:
        """
        Execute the ingestion using the configured strategy.

        Returns:
            Any: The raw response from the API.

        Raises:
            APIRequestError: If the ingestion strategy raises an error.
        """
        logger.info(
            f"Starting API ingestion using strategy: "
            f"{type(self._strategy).__name__}"
        )
        try:
            result = self._strategy.ingest()
            logger.info(
                "API ingestion completed successfully."
            )
            return result
        except Exception as e:
            logger.error(
                f"Failed to ingest using strategy "
                f"{type(self._strategy).__name__}: "
                f"{e}", exc_info=True
            )
            raise APIRequestError(
                type(self._strategy).__name__, e
            )

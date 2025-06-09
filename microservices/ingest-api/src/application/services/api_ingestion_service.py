from typing import Any, Dict, Optional

from src.domain.exceptions.exceptions import APIRequestError
from src.domain.ports.ingestion_strategy import APIIngestionStrategy
from src.infrastructure.logging.logger import get_logger

logger = get_logger(__name__)


class APIIngestion:
    """Context class for API ingestion, using strategy pattern."""

    def __init__(self, api_url: str, strategy: APIIngestionStrategy):
        """
        Initialize the APIIngestion context.

        Args:
            api_url (str): API endpoint URL.
            strategy (APIIngestionStrategy): Concrete ingestion strategy.
        """
        self.api_url = api_url
        self.strategy = strategy

    def ingest(self, params: Optional[Dict[str, Any]] = None) -> str:
        """
        Execute the ingestion using the provided strategy.

        Args:
            params (Optional[Dict[str, Any]]): Parameters to pass to the
            ingestion strategy.

        Returns:
            str: Raw response from the API.
        """
        try:
            return self.strategy.ingest(self.api_url, params)
        except Exception as e:
            logger.error(
                f"Failed to ingest using strategy for URL {self.api_url} "
                f"with params {params}: {e}"
            )
            raise APIRequestError(self.api_url, e)

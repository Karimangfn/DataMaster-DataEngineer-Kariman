from abc import ABC, abstractmethod
from typing import Any


class APIIngestionStrategy(ABC):
    """Base interface for API ingestion strategies."""

    @abstractmethod
    def ingest(self) -> Any:
        """
        Ingest data from the API source.

        Returns:
            Any: Raw response data from the API.
        """
        pass

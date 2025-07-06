from abc import ABC, abstractmethod
from typing import Any


class DatabaseIngestionStrategy(ABC):
    """Base interface for database ingestion strategies."""

    @abstractmethod
    def ingest(self) -> Any:
        """
        Ingest data from the database source.

        Returns:
            Any: Raw result extracted from the database.
        """
        pass

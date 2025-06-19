from abc import ABC, abstractmethod
from typing import Any, Dict, Optional


class APIIngestionStrategy(ABC):
    """Base interface for API ingestion strategies."""

    @abstractmethod
    def ingest(
        self,
        data_source: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, Any]] = None
    ) -> Any:
        """
        Ingest data from a given API source.

        Args:
            data_source (str): The URL of the data source.
            params (Optional[Dict[str, Any]]): Optional parameters
            to send in the query string.
            headers (Optional[Dict[str, Any]]): Optional headers
            to send with the request.

        Returns:
            Any: Raw response data from the API.
        """
        pass

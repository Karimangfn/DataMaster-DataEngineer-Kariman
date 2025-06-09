from typing import Any, Dict, Optional

import requests
from src.domain.exceptions.exceptions import APIIngestionError
from src.domain.ports.ingestion_strategy import APIIngestionStrategy
from src.infrastructure.logging.logger import get_logger

logger = get_logger(__name__)


class RestAPIIngestion(APIIngestionStrategy):
    """Ingests data from a REST API endpoint."""

    def ingest(
        self,
        data_source: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, Any]] = None
    ) -> Any:
        """
        Fetch data from a REST API.

        Args:
            data_source (str): The URL of the REST API.
            params (Optional[Dict[str, Any]]): Query parameters
            for the request.
            headers (Optional[Dict[str, Any]]): Headers for the
            request.

        Returns:
            Any: Raw text response from the API.

        Raises:
            APIIngestionError: If the request fails due to
            network or HTTP errors.
        """
        logger.debug(
            f"Sending GET request to {data_source} "
            f"with params={params} and headers={headers}"
        )
        try:
            response = requests.get(
                data_source,
                params=params,
                headers=headers,
                verify=False
            )
            response.raise_for_status()
            logger.info(
                f"Successfully ingested data from {data_source}"
            )
            return response.text
        except requests.exceptions.RequestException as e:
            logger.error(
                f"Request to {data_source} failed: {str(e)}"
            )
            raise APIIngestionError(
                f"Failed to ingest data from API {data_source}: {str(e)}",
                original_exception=e
            )

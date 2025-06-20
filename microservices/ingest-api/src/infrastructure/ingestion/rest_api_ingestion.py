from typing import Any

import requests
from src.domain.exceptions.exceptions import APIIngestionError
from src.domain.ports.authentication_strategy import AuthenticationStrategy
from src.domain.ports.ingestion_strategy import APIIngestionStrategy
from src.infrastructure.logging.logging_setup import get_logger

logger = get_logger(__name__)


class RestAPIIngestion(APIIngestionStrategy):
    """Ingests data from a REST API endpoint."""

    def __init__(self, url: str, auth_strategy: AuthenticationStrategy):
        """
        Initialize with API URL and auth strategy.

        Args:
            url (str): The API endpoint URL.
            auth_strategy (AuthenticationStrategy): Authentication strategy
            instance.
        """
        self.url = url
        self.auth_strategy = auth_strategy

    def ingest(self) -> Any:
        """
        Perform the GET request to the API with authentication.

        Returns:
            Any: The API response JSON.

        Raises:
            APIIngestionError: If the HTTP request to the API fails.
        """
        params = self.auth_strategy.get_query_params()
        headers = self.auth_strategy.get_headers()

        logger.debug(
            f"Sending GET request to {self.url} "
            f"with params={params} and headers={headers}"
        )

        try:
            response = requests.get(
                self.url,
                params=params,
                headers=headers,
                verify=False
            )
            response.raise_for_status()
            logger.info(
                f"Successfully ingested data from {self.url}"
            )
            return response.text
        except requests.exceptions.RequestException as e:
            logger.error(
                f"Request to {self.url} failed: {str(e)}",
                exc_info=True
            )
            raise APIIngestionError(
                f"Failed to ingest data from API {self.url}: "
                f"{str(e)}"
            )

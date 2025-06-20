# src/infrastructure/authentication/api_key_query_param.py
from typing import Dict

from src.domain.ports.authentication_strategy import AuthenticationStrategy


class APIKeyQueryParamAuth(AuthenticationStrategy):
    """
    Authentication strategy that adds an API key as a query parameter.
    """

    def __init__(self, key: str):
        """
        Initialize with the given API key.

        Args:
            key (str): API key to be used in the query string.
        """
        self.key = key

    def get_query_params(self) -> Dict[str, str]:
        """
        Return the API key as a query parameter.

        Returns:
            Dict[str, str]: Dictionary with the API key.
        """
        return {"key": self.key}

    def get_headers(self) -> Dict[str, str]:
        """
        Return headers related to authentication (none in this case).

        Returns:
            Dict[str, str]: Empty dictionary since this auth uses query params.
        """
        return {}

from abc import ABC, abstractmethod
from typing import Dict


class AuthenticationStrategy(ABC):
    """
    Interface for API authentication strategies that provide query parameters.
    """

    @abstractmethod
    def get_query_params(self) -> Dict[str, str]:
        """
        Return authentication-related query parameters to be appended
        to the API request.

        Returns:
            Dict[str, str]: Dictionary of query parameters.
        """
        pass

    @abstractmethod
    def get_headers(self) -> Dict[str, str]:
        """
        Return authentication-related headers to be included in
        the API request.

        Returns:
            Dict[str, str]: Dictionary of headers.
        """
        pass

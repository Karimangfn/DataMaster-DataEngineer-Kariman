from abc import ABC, abstractmethod
from typing import Any


class DatabaseConnectionStrategy(ABC):
    """
    Interface for database connection strategies.
    """

    @abstractmethod
    def get_connection(self) -> Any:
        """
        Return an active connection to the database.

        Returns:
            Any: A database connection object.
        """
        pass

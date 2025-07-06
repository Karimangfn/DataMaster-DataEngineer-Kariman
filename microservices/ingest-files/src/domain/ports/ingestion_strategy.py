from abc import ABC, abstractmethod


class IngestionStrategy(ABC):
    @abstractmethod
    def ingest(self, source_path: str, destination_path: str) -> None:
        """
        Defines the ingestion operation for a file.

        Args:
            source_path (str): Full path to the source file
            on the local system.
            destination_path (str): Full path where the file
            should be ingested (e.g., Azure Blob Storage path).
        """
        pass

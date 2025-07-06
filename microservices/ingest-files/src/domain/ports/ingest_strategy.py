from abc import ABC, abstractmethod


class IngestionStrategy(ABC):

    @abstractmethod
    def ingest(self, file_path: str):
        pass
from abc import ABC, abstractmethod

class IngestStrategy(ABC):

    @abstractmethod
    def ingest(self, file_path: str):
        pass
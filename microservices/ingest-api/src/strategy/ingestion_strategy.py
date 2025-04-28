from abc import ABC, abstractmethod


class APIIngestionStrategy(ABC):
    @abstractmethod
    def ingest(self, data_source):
        pass

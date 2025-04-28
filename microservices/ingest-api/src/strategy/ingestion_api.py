from .ingestion_rest_api import RestAPIIngestion


class APIIngestion:
    def __init__(self, api_url, api_type):
        self.api_url = api_url
        self.api_type = api_type.lower()
        self.strategy = self._get_strategy()

    _INGESTIONTYPES = {
        "rest": RestAPIIngestion
    }

    def _get_strategy(self):
        if self.api_type not in self._INGESTIONTYPES:
            raise ValueError(f"API type {self.api_type} not supported")
        return self._INGESTIONTYPES[self.api_type]()

    def ingest(self, params=None):
        return self.strategy.ingest(self.api_url, params)

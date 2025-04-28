import requests

from .ingestion_strategy import APIIngestionStrategy


class RestAPIIngestion(APIIngestionStrategy):
    def ingest(self, data_source, params=None, headers=None):
        try:
            response = requests.get(data_source,
                                    params=params,
                                    headers=headers,
                                    verify=False)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            raise RuntimeError(
                f"Erro ao ingerir dados da API {data_source}: {str(e)}"
            )

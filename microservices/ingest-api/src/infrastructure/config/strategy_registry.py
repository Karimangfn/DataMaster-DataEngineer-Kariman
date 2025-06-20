from typing import Dict, Type

from src.domain.ports.authentication_strategy import AuthenticationStrategy
from src.domain.ports.ingestion_strategy import APIIngestionStrategy
from src.infrastructure.authentication.query_param_auth import \
    APIKeyQueryParamAuth
from src.infrastructure.ingestion.rest_api_ingestion import RestAPIIngestion

INGESTION_STRATEGIES: Dict[str, Type[APIIngestionStrategy]] = {
    "rest": RestAPIIngestion
}

AUTH_STRATEGIES: Dict[str, Type[AuthenticationStrategy]] = {
    "query_param": APIKeyQueryParamAuth
}

from typing import Dict, Type

from src.domain.ports.authentication_strategy import AuthenticationStrategy
from src.domain.ports.ingestion_strategy import APIIngestionStrategy
from src.infrastructure.authentication.query_param_auth import \
    APIKeyQueryParamAuth
from src.infrastructure.ingestion.rest_api_ingestion import RestAPIIngestion

# Mapping of supported API ingestion strategies by type name
INGESTION_STRATEGIES: Dict[str, Type[APIIngestionStrategy]] = {
    "rest": RestAPIIngestion
}

# Mapping of supported API authentication strategies by type name
AUTH_STRATEGIES: Dict[str, Type[AuthenticationStrategy]] = {
    "query_param": APIKeyQueryParamAuth
}

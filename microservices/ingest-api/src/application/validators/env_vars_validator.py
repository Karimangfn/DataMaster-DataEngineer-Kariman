import os
from typing import Dict, List

from src.domain.exceptions.exceptions import MissingEnvironmentVariableError
from src.infrastructure.logging.logging_setup import get_logger

logger = get_logger(__name__)


def validate_env_vars(required_vars: List[str]) -> Dict[str, str]:
    """
    Validate the presence of required environment variables.

    Args:
        required_vars (List[str]): List of environment variable
        names to validate.

    Returns:
        Dict[str, str]: Dictionary mapping variable names to their values.

    Raises:
        MissingEnvironmentVariableError: If any required environment
        variable is missing or empty.
    """
    env_vars = {var: os.getenv(var) for var in required_vars}
    missing = [var for var, val in env_vars.items() if not val]
    if missing:
        logger.error(
            f"Missing environment variables: {missing}"
        )
        raise MissingEnvironmentVariableError(missing)
    return env_vars

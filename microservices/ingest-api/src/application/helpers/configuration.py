from pathlib import Path
from typing import Any, Dict

import yaml
from src.domain.exceptions.exceptions import ConfigurationLoadError
from src.infrastructure.logging.logging_setup import get_logger

logger = get_logger(__name__)


def load_config(config_filename: str) -> Dict[str, Any]:
    """
    Load configuration from a YAML file.

    Args:
        config_filename (str): Relative path to the YAML configuration file.

    Returns:
        Dict[str, Any]: Parsed configuration as dictionary.

    Raises:
        ConfigurationLoadError: If the file doesn't exist or has invalid YAML.
    """
    root_dir = Path(__file__).resolve().parents[2]
    config_path = root_dir / config_filename

    logger.info(
        f"Loading configuration from: {config_path}"
    )

    try:
        with open(config_path, "r", encoding="utf-8") as file:
            config = yaml.safe_load(file)
            logger.info(
                "Configuration loaded successfully."
            )
            return config
    except (FileNotFoundError, yaml.YAMLError) as e:
        logger.error(
            f"Failed to load configuration from {config_path}: {e}",
            exc_info=True
        )
        raise ConfigurationLoadError(
            str(config_path), e
        )

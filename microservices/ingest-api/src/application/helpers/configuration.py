from pathlib import Path
from typing import Any, Dict

import yaml
from src.domain.exceptions.exceptions import ConfigurationLoadError


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

    try:
        with open(config_path, "r", encoding="utf-8") as file:
            return yaml.safe_load(file)
    except (FileNotFoundError, yaml.YAMLError) as e:
        raise ConfigurationLoadError(str(config_path), e)

import os
import sys
import pytest
from unittest.mock import MagicMock

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC_DIR = os.path.join(ROOT_DIR, "src")
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)


@pytest.fixture
def spark():
    """
    Provides a mocked SparkSession for testing Gold layer.
    """
    mock_spark = MagicMock()
    return mock_spark

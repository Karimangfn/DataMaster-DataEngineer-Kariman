from src.config.settings import DATASET_CONFIG


def test_dataset_config_keys():
    """
    Testa se o dicionário DATASET_CONFIG contém todas as chaves necessárias
    para a pipeline Gold e se seus valores são strings.
    """
    required_keys = ["silver_path", "gold_path", "gold_checkpoint_path"]
    for key in required_keys:
        assert key in DATASET_CONFIG
        assert isinstance(DATASET_CONFIG[key], str)

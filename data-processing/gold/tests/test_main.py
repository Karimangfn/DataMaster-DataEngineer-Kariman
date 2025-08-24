from unittest.mock import patch
import src.main as main_module

def test_main_calls_transform_gold(spark):
    """
    Test that main() calls transform_gold with the correct SparkSession and paths.
    """
    with patch.object(main_module, "transform_gold", return_value=None) as mock_transform:
        main_module.spark = spark
        
        main_module.main()

        mock_transform.assert_called_once_with(
            spark,
            main_module.DATASET_CONFIG["silver_path"],
            main_module.DATASET_CONFIG["gold_path"]
        )

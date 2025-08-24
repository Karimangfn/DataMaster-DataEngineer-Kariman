from unittest.mock import patch
import src.main as main_module


def test_main_calls_transform_silver(spark):
    """
    Test that main() calls transform_silver with the correct SparkSession and paths.
    """
    with patch.object(main_module, "transform_silver", return_value=None) as mock_transform:
        main_module.spark = spark
        
        main_module.main()

        mock_transform.assert_called_once_with(
            spark,
            main_module.DATASET_CONFIG["bronze_path"],
            main_module.DATASET_CONFIG["silver_path"]
        )

import pytest
from pyspark.sql.types import (StructType, StructField, StringType, DateType,
                               DoubleType, TimestampType, BooleanType)
from src.modules.schemas import get_silver_schema


def test_get_silver_schema():
    """
    Test that get_silver_schema returns the expected schema with correct fields and types.
    """
    
    expected_fields = [
        ("customer_id", StringType),
        ("first_name", StringType),
        ("last_name", StringType),
        ("email", StringType),
        ("purchase_date", DateType),
        ("total_amount", DoubleType),
        ("product", StringType),
        ("store_location", StringType),
        ("cpf_masked", StringType),
        ("credit_card_masked", StringType),
        ("source_file_name", StringType),
        ("ingestion_timestamp", TimestampType),
        ("raw_ingestion_id", StringType),
        ("high_value_purchase", BooleanType)
    ]

    schema = get_silver_schema()
    assert isinstance(schema, StructType)
    assert len(schema.fields) == len(expected_fields)

    for field, (expected_name, expected_type) in zip(schema.fields, expected_fields):
        assert field.name == expected_name
        assert isinstance(field.dataType, expected_type)
        assert field.nullable is True

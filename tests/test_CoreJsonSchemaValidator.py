import pytest
from akm_tools.validation.data_instance_validators import CoreJsonSchemaValidator


# Testing CoreJsonSchemaValidator with simple data
def test_simple_data_validator_with_valid_data(simple_schema, simple_data):
    simple_data_validator = CoreJsonSchemaValidator(schema=simple_schema, extended_schema_dir=None)
    valid_data = []
    for instance in simple_data:
        is_valid, _ = simple_data_validator.validate(instance=instance)
        valid_data.append(is_valid)
    assert all(valid_data) == True


def test_simple_data_validator_with_invalid_data(simple_schema, simple_data_with_more_attributes):
    simple_data_validator = CoreJsonSchemaValidator(schema=simple_schema, extended_schema_dir=None)
    valid_data = []
    for instance in simple_data_with_more_attributes:
        is_valid, _ = simple_data_validator.validate(instance=instance)
        valid_data.append(is_valid)
    assert all(valid_data) == False


def test_simple_data_validator_with_data_missing_attributes(simple_schema, simple_data_without_required_attribute):
    simple_data_validator = CoreJsonSchemaValidator(schema=simple_schema, extended_schema_dir=None)
    valid_data = []
    for instance in simple_data_without_required_attribute:
        is_valid, _ = simple_data_validator.validate(instance=instance)
        valid_data.append(is_valid)
    assert all(valid_data) == False


def test_complex_data_validator_with_jsonschema_references(complex_schema_with_defs, complex_data):
    """
    check if using references with $id works (a jsonschema feature)
    """
    schema, registry = complex_schema_with_defs
    complex_data_validator = CoreJsonSchemaValidator(schema=schema, extended_schema_dir=None)
    complex_data_validator.configure_registry(registry)
    valid_data = []
    for instance in complex_data:
        is_valid, _ = complex_data_validator.validate(instance=instance)
        valid_data.append(is_valid)
    assert all(valid_data) == True


def test_complex_data_validator_with_missing_required_attributes(
    complex_schema_with_defs, complex_data_missing_required_attributes
):
    schema, registry = complex_schema_with_defs
    complex_data_validator = CoreJsonSchemaValidator(schema=schema, extended_schema_dir=None)
    complex_data_validator.configure_registry(registry)
    valid_data = []
    for instance in complex_data_missing_required_attributes:
        is_valid, _ = complex_data_validator.validate(instance=instance)
        valid_data.append(is_valid)
    assert all(valid_data) == False


def test_complex_data_validator_with_invalid_attribute(complex_schema_with_defs, complex_data_with_additional_attributes):
    schema, registry = complex_schema_with_defs
    complex_data_validator = CoreJsonSchemaValidator(schema=schema, extended_schema_dir=None)
    complex_data_validator.configure_registry(registry)
    valid_data = []
    for instance in complex_data_with_additional_attributes:
        is_valid, _ = complex_data_validator.validate(instance=instance)
        valid_data.append(is_valid)
    assert all(valid_data) == False


def test_complex_data_validator_with_extended_data(scehma_with_extensions, data_with_extended_properties):
    schema, registry = scehma_with_extensions
    complex_data_validator = CoreJsonSchemaValidator(schema=schema, extended_schema_dir=None)
    complex_data_validator.configure_registry(registry)
    valid_data = []
    for instance in data_with_extended_properties:
        is_valid, _ = complex_data_validator.validate(instance=instance)
        valid_data.append(is_valid)
    assert all(valid_data) == True


def test_complex_data_validator_with_extended_data(scehma_with_extensions, overlay_existing_data_with_addional_properties):
    schema, registry = scehma_with_extensions
    complex_data_validator = CoreJsonSchemaValidator(schema=schema, extended_schema_dir=None)
    complex_data_validator.configure_registry(registry)
    valid_data = []
    for instance in overlay_existing_data_with_addional_properties:
        is_valid, _ = complex_data_validator.validate(instance=instance)
        valid_data.append(is_valid)
    assert all(valid_data) == True

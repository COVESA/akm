import pytest
from akm_tools.validation.data_context_validators import ExtendedInstanceContentValidator
from akm_tools.validation.custom_exceptions import BaseInstanceOverwiteException, IDConflictException
from akm_tools.validation.global_debug_config import GlobalDebugConfig


def test_extended_data_is_valid(overlay_existing_data_with_addional_properties):
    assert ExtendedInstanceContentValidator.check_data_is_extended_not_overwritten(
        overlay_existing_data_with_addional_properties
    )


def test_extended_data_is_used(overlay_existing_data_with_addional_properties):
    validator = ExtendedInstanceContentValidator()
    valid_data = validator.validate_data_contexts(overlay_existing_data_with_addional_properties)
    assert valid_data[0] == {
        "id": "unique_id1",
        "entityType": "ObjectType3",
        "extended_property": "any string",
    }
    assert len(validator.warning_messages) == 1
    assert len(validator.error_messages) == 0


def test_overriding_base_data_not_allowed(ovewrite_existing_data):
    validator = ExtendedInstanceContentValidator()
    valid_data = validator.validate_data_contexts(ovewrite_existing_data)
    assert valid_data[0] == {
        "id": "unique_id1",
        "description": "description for unique_id1",
        "entityType": "ObjectType3",
    }
    assert len(validator.warning_messages) == 0
    assert len(validator.error_messages) == 1


def test_overriding_base_data_in_debug_mode_raises_exception(ovewrite_existing_data):
    GlobalDebugConfig.set_debug_mode()
    validator = ExtendedInstanceContentValidator()
    try:
        valid_data = validator.validate_data_contexts(ovewrite_existing_data)
        pytest.fail("BaseInstanceOverwiteException was not raised when expected.")
    except BaseInstanceOverwiteException as e:
        assert True
    except Exception as e:
        pytest.fail(f"Unexpected exception type raised: {type(e).__name__}")

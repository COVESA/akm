import pytest
from akm_tools.validation.data_context_validators import CrossReferenceValidator


@pytest.fixture
def invalid_chain_of_references():
    return [
        {"id": "Component1", "entityTypeID": "Class1", "isA": {"referentEntityTypeID": "Class1", "referentID": "Object1"}},
        {
            "id": "Object1",
            "definition": "A component of a vehicle",
            "entityTypeID": "Class1",
            "isA": {"referentEntityTypeID": "Class1", "referentID": "Not_defined_Component"},
        },
        {
            "id": "Component2",
            "entityTypeID": "Class1",
            "isA": {"referentEntityTypeID": "Class1", "referentID": "Component1"},
        },
    ]


@pytest.fixture
def valid_chain_of_reference():
    return [
        {"id": "Component1", "entityTypeID": "Class1", "isA": {"referentEntityTypeID": "Class1", "referentID": "Object1"}},
        {
            "id": "Object1",
            "entityTypeID": "Class1",
        },
        {"id": "Component2", "entityTypeID": "Class1", "isA": {"referentEntityTypeID": "Class1", "referentID": "Object1"}},
    ]


@pytest.fixture
def reference_not_present():
    return [
        {"id": "Component1", "entityTypeID": "Class1", "isA": {"referentEntityTypeID": "Class1", "referentID": "Object1"}},
        {"id": "Component2", "entityTypeID": "Class1", "isA": {"referentEntityTypeID": "Class1", "referentID": "Object1"}},
    ]


@pytest.fixture
def circular_references():
    return [
        {"id": "Object1", "entityTypeID": "Class1", "isA": {"referentEntityTypeID": "Class1", "referentID": "Component1"}},
        {"id": "Component1", "entityTypeID": "Class1", "isA": {"referentEntityTypeID": "Class1", "referentID": "Object1"}},
    ]


def test_invalid_chain_of_references(invalid_chain_of_references):
    validator = CrossReferenceValidator()
    valid_data = validator.validate_data_contexts(invalid_chain_of_references)
    assert len(valid_data) == 0, "The validator should return False for all instances"


def test_valid_chain_of_reference(valid_chain_of_reference):
    validator = CrossReferenceValidator()
    valid_data = validator.validate_data_contexts(valid_chain_of_reference)
    assert len(valid_data) == 3, "The validator should return True for valid cross-references"


def test_reference_not_present(reference_not_present):
    validator = CrossReferenceValidator()
    valid_data = validator.validate_data_contexts(reference_not_present)
    assert len(valid_data) == 0, "The validator should return False for all instances"


def test_circular_references(circular_references):
    validator = CrossReferenceValidator()
    assert validator.validate_data_contexts(circular_references) == []

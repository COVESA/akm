import pytest
from akm_tools.validation.custom_exceptions import (
    IDConflictException,
    BaseInstanceOverwiteException,
    InvalidReferentIDException,
)


def test_IDConflictException():
    """
    This error should be raised when there is more than 3 instances with the same ID
    """
    instances = [{"id": 1}, {"id": 1}, {"id": 1}]
    with pytest.raises(IDConflictException) as excinfo:
        raise IDConflictException(instances)
    assert str(excinfo.value) == f"More than 2 instances with same  ID ! \n{instances}\n"


def test_BaseInstanceOverwiteException():
    """
    This error should be raised when an extended instance is overwriting properties of a base instance
    """
    base_instance = {"id": "data_instance1"}
    extended_instance = {"id": "data_instance2", "name": "test"}
    with pytest.raises(BaseInstanceOverwiteException) as excinfo:
        raise BaseInstanceOverwiteException(base_instance, extended_instance)
    assert (
        str(excinfo.value)
        == f"The extended instance :\n{extended_instance}\nis overwriting properties of base instance\n{base_instance}\n"
    )


def test_InvalidReferentIDException():
    """
    This error should be raised when data instace refers to an invalid id
    """
    instance = {"id1": 1, "isA": {"referentEntityTypeID": "FeatureOfInterestClass", "referentID": "non_existing_id"}}
    referentID_value = instance["isA"]["referentID"]
    with pytest.raises(InvalidReferentIDException) as excinfo:
        raise InvalidReferentIDException(instance, referentID_value)
    assert str(excinfo.value) == f"The instance :\n{instance}\nis referencing an invalid id : '{referentID_value}'\n"

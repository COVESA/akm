import pytest
from akm_tools.validation.data_context_validators import AllDataContextValidators


def test_create_instance_dict():
    """
    Test case for the create_instance_dict method of the AllDataContextValidators class.

    This test checks if the create_instance_dict method correctly creates a dictionary
    that maps instance id's to a dictionary containing the count of instances with that ID
    and a list of the instances themselves.
    """
    all_data = [{"id": "1a", "name": "test1"}, {"id": "2b", "name": "test2"}, {"id": "1a", "name": "test3"}]
    instance_dict = AllDataContextValidators.create_instance_dict(all_data)
    expected_dict = {
        "1a": {"count": 2, "instances": [{"id": "1a", "name": "test1"}, {"id": "1a", "name": "test3"}]},
        "2b": {"count": 1, "instances": [{"id": "2b", "name": "test2"}]},
    }
    assert instance_dict == expected_dict, "The instance dictionary was not created correctly."

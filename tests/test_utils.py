import pytest
import yaml
import io
from akm_tools.utils.genutils import YamlCustomDumper


@pytest.fixture
def yaml_data():
    return [{"a": 1, "b": 2}, {"c": 3, "d": 4}]


@pytest.fixture
def expected_yaml_string():
    yaml_string = """
- a: 1
  b: 2

- c: 3
  d: 4
"""
    return yaml_string.lstrip()


def test_YamlCustomDumper_dumps(yaml_data, expected_yaml_string):
    """
    This test checks if the dumps method correctly converts a list of dictionaries to a YAML string, with a line break after each instance.
    """
    yaml_string = YamlCustomDumper.dumps(yaml_data)
    assert yaml_string == expected_yaml_string, "The YAML string is properly formatted with a line break"


def test_YamlCustomDumper_dump(yaml_data, expected_yaml_string):
    """
    This test checks if the dump method correctly converts a list of dictionaries to a YAML string, with a line break after each instance.
    """
    file = io.StringIO()
    YamlCustomDumper.dump(yaml_data, file)

    # Check if the file was written correctly
    file.seek(0)
    yaml_string = file.read()
    assert yaml_string == expected_yaml_string, "The file was written correctly."

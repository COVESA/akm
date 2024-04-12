import pytest
from referencing.jsonschema import DRAFT202012
from referencing import Registry, Resource

## Assumptions/Requiremets : All types of schema will have ['id','type'] present and required for objects


@pytest.fixture
def simple_schema():
    schema = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": "https://somehost.com/test.scehma.json",
        "type": "object",
        "properties": {
            "type": {"type": "string"},
            "age": {"type": "number"},
            "id": {"type": "string"},
        },
        "required": ["id"],
        "additionalProperties": False,
    }
    return schema


@pytest.fixture
def simple_data():
    data = [
        {"type": "John", "age": 30, "id": "unique_id_1"},
        {"type": "Jane", "age": 25, "id": "unique_id_2"},
    ]
    return data


@pytest.fixture
def simple_data_with_more_attributes():
    data = [
        {"type": "John", "age": 30, "id": "unique_id_1", "extra_attribute": "wild"},
        {"type": "Jane", "age": 25, "id": "unique_id_2", "extra_attribute": "grass"},
    ]
    return data


@pytest.fixture
def simple_data_without_required_attribute():
    data = [{"type": "John", "age": 30}, {"type": "Jane", "age": 25}]
    return data


@pytest.fixture
def complex_schema_with_defs():
    schema = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": "complexSchema",
        "oneOf": [
            {"$ref": "complexSchema.ObjectType1"},
            {"$ref": "complexSchema.ObjectType2"},
        ],
        "$defs": {
            "BaseClass": {
                "$id": "complexSchema.BaseClass",
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "definition": {"type": "string"},
                },
                "required": ["id"],
            },
            "ObjectType1": {
                "$id": "complexSchema.ObjectType1",
                "type": "object",
                "allOf": [{"$ref": "complexSchema.BaseClass"}],
                "properties": {
                    "name": {"type": "string"},
                    "description": {"type": "string"},
                    "type": {"type": "string", "const": "ObjectType1"},
                },
                "required": ["name", "type"],
                "unevaluatedProperties": False,
            },
            "ObjectType2": {
                "$id": "complexSchema.ObjectType2",
                "type": "object",
                "allOf": [{"$ref": "complexSchema.BaseClass"}],
                "properties": {
                    "age": {"type": "number"},
                    "type": {"type": "string", "const": "ObjectType2"},
                },
                "required": ["type"],
                "unevaluatedProperties": False,
            },
        },
    }
    schema_resources = [("complex_scehma", DRAFT202012.create_resource(schema))]
    registry = Registry().with_resources(schema_resources)
    return schema, registry


@pytest.fixture
def complex_data():
    data = [
        {
            "id": "unique_id_1",
            "definition": "Some def1",
            "name": "AttributeName",
            "type": "ObjectType1",
            "description": "some desc",
        },
        {"id": "unique_id_2", "type": "ObjectType2", "age": 10},
    ]
    return data


@pytest.fixture
def complex_data_missing_required_attributes():  ## id/type is missing.
    data = [
        {
            "definition": "Some def1",
            "name": "AttributeName",
            "type": "ObjectType1",
            "description": "some desc",
        },
        {
            "type": "ObjectType2",
            "age": 10,
        },
    ]
    return data


@pytest.fixture
def complex_data_with_additional_attributes():
    data = [
        {
            "id": "unique_id_1",
            "definition": "Some def1",
            "name": "AttributeName",
            "type": "ObjectType1",
            "description": "some desc",
            "extra_attribute": "wild",
        },
        {
            "id": "unique_id_2",
            "type": "ObjectType2",
            "age": 10,
            "extra_attribute": "grass",
        },
    ]
    return data


@pytest.fixture
def data_with_duplicate_ids():
    data = [
        {
            "id": "unique_id_1",
            "definition": "Some def1",
            "name": "AttributeName",
            "type": "ObjectType1",
            "description": "some desc",
        },
        {
            "id": "unique_id_1",
            "definition": "Some def2",
            "name": "AttributeName2",
            "type": "ObjectType2",
            "description": "some desc2",
        },
    ]
    return data


@pytest.fixture
def scehma_with_extensions():
    schema = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": "schema_with_extensions",
        "type": "object",
        "allOf": [
            {"$ref": "extension.additional_properties"},
        ],
        "properties": {
            "id": {"type": "string"},
            "description": {"type": "string"},
            "entityType": {"type": "string", "const": "ObjectType3"},
        },
        "required": ["entityType"],
        "unevaluatedProperties": False,
    }
    schema_extension = {
        "$id": "extension.additional_properties",
        "type": "object",
        "properties": {"extended_property": {"type": "string"}},
    }
    schema_resources = [
        ("complex_scehma", DRAFT202012.create_resource(schema)),
        ("schema_extension", DRAFT202012.create_resource(schema_extension)),
    ]
    registry = Registry().with_resources(schema_resources)
    return schema, registry


@pytest.fixture
def data_with_extended_properties():
    data = [
        {
            "id": "unique_id1",
            "entityType": "ObjectType3",
            "extended_property": "any string",
        }
    ]
    return data


@pytest.fixture
def overlay_existing_data_with_addional_properties():
    data = [
        {
            "id": "unique_id1",
            "entityType": "ObjectType3",
        },
        {
            "id": "unique_id1",
            "entityType": "ObjectType3",
            "extended_property": "any string",
        },
    ]
    return data


@pytest.fixture
def ovewrite_existing_data():
    data = [
        {
            "id": "unique_id1",
            "description": "description for unique_id1",
            "entityType": "ObjectType3",
        },
        {
            "id": "unique_id1",
            "entityType": "CHANGED",
            "description": "description CHANGED",
            "extended_property": "any string",
        },
    ]
    return data

import pytest
from referencing.jsonschema import DRAFT202012
from referencing import Registry, Resource

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
            "entityTypeID": {"type": "string"},
        },
        "required": ["id", "entityTypeID"],
        "additionalProperties": False,
    }
    return schema


@pytest.fixture
def simple_data():
    data = [
        {"type": "John", "age": 30, "id": "unique_id_1", "entityTypeID": "type1"},
        {"type": "Jane", "age": 25, "id": "unique_id_2", "entityTypeID": "type2"},
    ]
    return data


@pytest.fixture
def simple_data_with_more_attributes():
    data = [
        {"type": "John", "age": 30, "id": "unique_id_1", "entityTypeID": "type1", "extra_attribute": "wild"},
        {"type": "Jane", "age": 25, "id": "unique_id_2", "entityTypeID": "type2", "extra_attribute": "grass"},
    ]
    return data


@pytest.fixture
def simple_data_without_required_attribute():
    data = [
        {"type": "John", "age": 30, "entityTypeID": "type1"},
        {"type": "Jane", "age": 25, "entityTypeID": "type2"}
    ]
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
                    "entityTypeID": {"type": "string"},
                    "definition": {"type": "string"},
                },
                "required": ["id", "entityTypeID"],
            },
            "ObjectType1": {
                "$id": "complexSchema.ObjectType1",
                "type": "object",
                "allOf": [{"$ref": "complexSchema.BaseClass"}],
                "properties": {
                    "name": {"type": "string"},
                    "description": {"type": "string"},
                },
                "required": ["name"],
                "unevaluatedProperties": False,
            },
            "ObjectType2": {
                "$id": "complexSchema.ObjectType2",
                "type": "object",
                "allOf": [{"$ref": "complexSchema.BaseClass"}],
                "properties": {
                    "age": {"type": "number"},
                },
                "required": ["age"],
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
            "entityTypeID": "type1",
            "definition": "Some def1",
            "name": "AttributeName",
            "description": "some desc",
        },
        {"id": "unique_id_2", "entityTypeID": "type2",  "age": 10},
    ]
    return data


@pytest.fixture
def complex_data_missing_required_attributes():  ## id/entityTypeID is missing.
    data = [
        {
            "definition": "Some def1",
            "name": "AttributeName",
            "description": "some desc",
        },
        {
            "age": 10,
        },
    ]
    return data


@pytest.fixture
def complex_data_with_additional_attributes():
    data = [
        {
            "id": "unique_id_1",
            "entityTypeID": "typObjectType1e1",
            "definition": "Some def1",
            "name": "AttributeName",
            "description": "some desc",
            "extra_attribute": "wild",
        },
        {
            "id": "unique_id_2",
            "entityTypeID": "ObjectType2",
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
            "entityTypeID": "type1",
            "definition": "Some def1",
            "name": "AttributeName",
            "description": "some desc",
        },
        {
            "id": "unique_id_1",
            "entityTypeID": "type1",
            "definition": "Some def2",
            "name": "AttributeName2",
            "description": "some desc2",
        },
    ]
    return data


@pytest.fixture
def schema_with_extensions():
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
            "entityTypeID": {"type": "string", "const": "ObjectType3"},
        },
        "required": ["id","entityTypeID"],
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
            "entityTypeID": "ObjectType3",
            "extended_property": "any string",
        }
    ]
    return data


@pytest.fixture
def overlay_existing_data_with_addional_properties():
    data = [
        {
            "id": "unique_id1",
            "entityTypeID": "ObjectType3",
        },
        {
            "id": "unique_id1",
            "entityTypeID": "ObjectType3",
            "extended_property": "any string",
        },
    ]
    return data


@pytest.fixture
def overwrite_existing_data():
    data = [
        {
            "id": "unique_id1",
            "entityTypeID": "ObjectType3",
            "description": "description for unique_id1",
        },
        {
            "id": "unique_id1",
            "entityTypeID": "ObjectType3",
            "description": "description CHANGED",
            "extended_property": "any string",
        },
    ]
    return data

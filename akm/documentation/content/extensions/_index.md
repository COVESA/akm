
---
title: Extensions
weight: 50
chapter: true
---

# Extensions
Extensions enable organizations to append new schema elements and data to the AKM.  Schema extensions are added to the akm/extensions/schema folder and data extensions are added to the akm/extensions/data folder.

The AKM adheres to the Open/Closed principle and does not provide a mechanism for overriding or redefining entries in the public AKM, which would invalidate the nature of a shared vocabulary.


## Example
The following example demonstrates how the Data Type is extended to include the corresponding json and xsd data types.
#### akm/extensions/schema/data_type.json
 ```JSON
{
  "$id": "akm.extension.DataType",
  "type": "object",
  "description": "Extended properties for DataType",
  "properties": {
    "jsonDataType": {
      "type": "string",
      "description": "The JSON data type as that correlates to this data type"
    },
    "xsdDataType": {
      "type": "string",
      "description": "The XML Schema data type as that correlates to this data type"
    }
  },
  "required": []
}
```
#### akm/extensions/data_types.json
 ```JSON
{
  "id": "boolean",
  "name": "boolean",
  "definition": "A binary data type that represents two possible values- true or false",
  "entityTypeID": "DataType",
  "jsonDataType": "boolean",
  "xsdDataType": "xsd:boolean"
}
```
 ```JSON
{
  "id": "int16",
  "name": "int16",
  "definition": "16-bit signed integer for range -32768 to 32767",
  "entityTypeID": "DataType",
  "jsonDataType": "json:integer",
  "xsdDataType": "xsd:short",
  "min": -32768,
  "max": 32767
}
```
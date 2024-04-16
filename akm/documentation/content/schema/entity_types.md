


---
title: "Entity Types"
date: 2019-08-04T13:05:11+02:00
weight: 1
---

### Main Entity Types
There are three main entity types:
- A ***Feature of Interest*** is a thing whose state or condition can be observed or manipulated. 
  Examples include the vehicle, driver, steering wheel, and tailgate.

- A ***Property*** is an attribute or characteristic that can describe one or more features of interest.  Examples include speed, compass direction, temperature, and whether a switch is set to on or off.

- A ***Metric*** is a type of signal that specifies a particular property of a particular feature of interest.  Examples include the vehicle identification number, the direction that the vehicle is heading, the ambient temperature in the cabin, and whether the driver door is locked.

>**Note:** The catalog does **not** include the actual measurements with the values of the metrics, such as:
>- The vehicle is traveling at ***84** kilometers per hour*.
>- The transmission is currently in ***third** gear*.
>- The driver's door is ***unlocked***.
>- The vehicle identification number is "***1FT7X2BT5CEC66117***".

**Note**:  AKM provides for representations of other signal schemas such as the [Vehicle Signal Specification](https://covesa.github.io/vehicle_signal_specification/introduction/overview/) (VSS) or CAN Bus, as well as conversions between their values.  Thus, it can both generate and understand signals from these schemas.

### Supporting Entity Types

#### General Supporting Entity Types
- An ***Entity*** is an abstract superclass that other entity types inherit from.  It provides the requirement that every object will have an identifier, name, and definition. It also defines other common properties such as comment and deprecation.

- An ***EntityType*** is a metatype that classifies other types of objects.  As described in this document, there are entity types for *Feature of Interest*, *Property*, *Data Type*, etc.    The data model can be extended by adding new entity types.

- A ***Representation*** describes an equivalent signal as it exists in another schema.  The *Metric* entity type can include an array of *Representations*.

- A ***Deprecation*** object can be embedded into metadata entries to document entries that are no longer maintained and/or supported.

#### Data Property Supporting Entity Types

- A ***Data Type*** is a classification of data elements that prescribes which values they can take, their size, and what type of mathematical, relational, or logical operations can be applied to them.  Examples include boolean, string, and numeric types such as int32, uint16, double, and float. 

- A ***Unit*** is a standard within a governed system by which a quantity can be expressed and universally understood.  Examples include units of measurement such as kilometer, liter, and degree Celsius; as well as units of concentration such as percent and parts per million. 

## Vehicle Metrics Metadata
The AKM includes instances of many objects commonly used in the vehicle signal domain. Because these objects share the standardized structure and meaning declared in the data model, they can be shared between organizations with no loss of meaning.  

### Examples

#### Driver Seatbelt (Feature of Interest)
 ```JSON
{
  "id": "Seatbelt.Row1.DriverSide",
  "name": "Seatbelt at Row 1 Driver Side",
  "definition": "Seatbelt at Row 1 Driver Side",
  "entityTypeID": "FeatureOfInterest",
  "partOf": {
    "entityTypeID": "FeatureOfInterest",
     "id": "Seat.Row1.DriverSide"
  },
  "isA": {
    "entityTypeID": "FeatureOfInterestClass",
    "id": "Seatbelt"
  }
}
```

#### Is Fastened (Boolean Data Property)
 ```JSON
{
  "id": "IsFastened",
  "name": "Is Fastened",
  "definition": "A boolean variable indicating that the subject has affixed its mating mechanical parts to securely connect its corresponding components",
  "entityTypeID": "DataProperty",
  "dataType": {
    "entityTypeID": "DataType",
  "  id": "boolean"
  }
}
```
#### Driver Seatbelt is Fastened (Metric)
 ```JSON
{
  "id": "Seatbelt.Row1.DriverSide.IsFastened",
  "name": "Seatbelt at Row1 Driver Side Is Fastened",
  "definition": "A boolean variable indicating whether the Front Driver Seatbelt Is Fastened",
  "entityTypeID": "Metric",
  "featureOfInterest": {
    "referentEntityTypeID": "FeatureOfInterest",
    "referentID": "Seatbelt.Row1.DriverSide"
  },
  "property": {
    "referentEntityTypeID": "Property",
    "referentID": "IsFastened"
  }
}

```
#### Latitude (Numeric Data Property)
 ```JSON
{
  "id": "Latitude",
  "name": "Latitude",
  "definition": "The angle between the equatorial plane and the straight line that passes through that point and through the center of the Earth determining how far north or south a location is",
  "entityTypeID": "DataProperty",
  "dataType": {
    "entityTypeID": "DataType",
  "  id": "double"
  },
  "defaultUnit": {
    "entityTypeID": "Unit",
  "  id": "degree"
  },
  "min": -180,
  "max": 180
}
```
#### Battery Type (Object Property)
 ```JSON
{
  "id": "BatteryType",
    "name": "Battery Type",
    "definition": "A category of electric battery based on such things as the use of different metals and electrolytes",
    "entityTypeID": "ObjectProperty",
    "values": [
    "LEAD_ACID",
    "LITHIUM_COBALT_OXIDE",
    "LITHIUM_ION_POLYMER",
    "LITHIUM_IRON_PHOSPHATE",
    "LITHIUM_MANGANESE",
    "LITHIUM_TITANATE_OXIDE",
    "NICKEL_METAL_HYDRIDE",
    "OTHER",
    "TERNARY_MATERIAL"  ]
}
```

## Scope

### In Scope
* Standardized schema for objects in the vehicle signal domain
* Set of common objects in the vehicle signal domain

### Out of Scope for Now
 - Diagnostic signals

### Out of Scope
* Message formats and other implementation details

 
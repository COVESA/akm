---
title: "Classes"
date: 2019-08-04T13:05:11+02:00
weight: 1
---

### Main Classes
There are three main classes of objects:
- A ***Feature of Interest*** is a thing whose state or condition can be observed or manipulated. 
  Examples include the vehicle, driver, steering wheel, or tailgate.

- A ***Property*** is an attribute or characteristic that can describe one or more features of interest.  Examples include speed, compass direction, temperature, whether a switch is set to on or off.

- A ***Metric*** combines a feature of interest and a property.  Examples include which direction the vehicle identification number, the direction that the vehicle is heading, the temperature in the cabin, and whether the driver door is locked.

>**Note:** The catalog does **not** include the actual measurements with the values of the metrics, such as:
>- The vehicle is traveling at ***84** kilometers per hour*.
>- The transmission is currently in ***third** gear*.
>- The driver's door is ***unlocked***.
>- The vehicle identification number is "***1FT7X2BT5CEC66117***".

>**Note**:  AKM reuses the identifiers from the [Vehicle Signal Specification](https://covesa.github.io/vehicle_signal_specification/introduction/overview/) (VSS) for its metrics and for most of its features of interest, and provides for conversions where the VSS could not be accommodated.  Thus, it can both generate and understand VSS entries.

### Supporting Classes

#### General Supporting Classes
- A ***Class*** is a meta-object that classifies other types of objects.  
    For instance, there are classes for *Feature of Interest*, *Property*, *Data Type*, etc. 
    The data model can be extended by adding new classes.

- A ***Conversions*** array can be embedded into metadata entries to map between AKM and other schemas.

- A ***Deprecation*** object can be embedded into metadata entries to document entries that are no longer maintained and/or supported

#### Data Property Supporting Classes

- A ***Data Type*** is a classification of data elements that prescribes which values they can take and what type of mathematical, relational, or logical operations can be applied to them.  Examples include boolean, string, and numeric types such as integer, double, and float. 

- A ***Unit*** is a standard within a governed system by which a quantity can be expressed and universally understood.  Examples include units of measurement such as kilometer, liter, and degree Celsius; as well as units of concentration such as percent and parts per million. 

## Vehicle Metrics Metadata
The AKM includes instances of many objects commonly used in the vehicle signal domain. Because these objects share the standardized structure and meaning declared in the data model, they can be shared between organizations with no loss of meaning.  

### Examples

#### Driver Seatbelt is Fastened (Metric)
 ```JSON
 "Vehicle.Cabin.Seat.Row1.DriverSide.IsBelted": {
    "name": "Seatbelt Is Fastened at Row 1 Driver Side",
    "class": "Metric",
    "definition": "Indicates whether the Seatbelt Is Fastened at Row 1 Driver Side",
    "featureOfInterest": "Vehicle.Cabin.Seat.Seatbelt.Row1.DriverSide",
    "property": "IsFastened"
  }
```
#### Driver Seatbelt (Feature of Interest)
 ```JSON
  "Vehicle.Cabin.Seat.Seatbelt.Row1.DriverSide": {
    "name": "Seatbelt at Row 1 Driver Side",
    "class": "FeatureOfInterest",
    "definition": "Seatbelt at Row 1 Driver Side",
    "isA": "Vehicle.Cabin.Seat.Seatbelt",
    "partOf": "Vehicle.Cabin.Seat.Row1.DriverSide"
  }
```

#### Is Fastened (Boolean Data Property)
 ```JSON
  "IsFastened": {
    "name": "Is Fastened",
    "class": "DataProperty",
    "definition": "A boolean variable indicating that the subject has affixed mating mechanical parts to securely connect its corresponding components",
    "dataType": "boolean"
  }
```
#### Latitude (Numeric Data Property)
 ```JSON
  "Latitude": {
    "name": "Latitude",
    "class": "DataProperty",
    "definition": "The angle between the equatorial plane and the straight line that passes through that point and through the center of the Earth determining how far north or south a location is",
    "dataType": "double",
    "unit": "degrees",
    "min": "-180",
    "max": "180"
  }
```
#### Date Format (Object Property)
 ```JSON
  "DateFormat": {
    "name": "Date Format",
    "class": "ObjectProperty",
    "definition": "A means of representing a date",
    "instances": [
        "YYYY-MM-DD",
        "DD-MM-YYYY",
        "MM-DD-YYYY",
        "YY-MM-DD",
        "DD-MM-YY",
        "MM-DD-YY"
      ]
  }
```

## Scope

### In Scope
* Standardized schema for objects in the vehicle signal domain
* Set of common objects in the vehicle signal domain

### Out of Scope for Now
 - Diagnostic signals
 - Weather, roads, and other externalities

### Out of Scope
* Message formats and other implementation details


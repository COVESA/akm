
---
title: "Principles"
chapter: true
weight: 20
---

# Principles

This page covers some of the principles that guided the creation of the AKM and that should be followed when contributing to it.


## Data-Centric
A layered design that separates data from algorithms increases opportunities for extension, reuse, and independent development.  The AKM is intended to represent the things that exist in the vehicle information domain with no bias toward any particular use by vehicle or software components. The following practices support this principle:
- Every entry within the AKM has an explicit unique identifier so it can be directly accessed
- References from one entry to another are explicitly expressed rather than encoded within a field or implied by other means such as its position in a file or folder.
- The AKM makes no assumptions about query patterns and is expressive enough to derive graphs, tables, trees, various types of files, and other derived structures deemed useful.

## Connected 
Vehicle information is highly connected, so the AKM allows objects to refer to related objects.  Examples include:
- Part-to-Whole relationships using the ***partOf*** property
  - The driver's seatbelt can refer to the driver's seat that contains it.
  - The radio can indicate that it is part of the infotainment system.
- Generalization inheritance using the ***isA*** property
  - The front passenger HVAC station can indicate that it is a HVAC station.
  - The rear driver-side door can indicate that it is a cabin door.
- Peer-to-peer associations
  - The VehicleTravel.Speed metric can indicate that its feature of interest is VehicleTravel, and that its property is Speed.
  - The Speed property can indicate that its default unit of measurement is kilometer per hour, and that its data type is float.

## Atomic
An atomic concept is the smallest unit of meaning that can be modeled.   Separating concepts into their atomic components allows for more flexibility, accuracy, and efficiency in storing and querying data.  The AKM maintains separate objects for metrics, features of interest, data and object properties, units of measurement, and data types.  It includes embedded objects for deprecation facts and mappings to other schemas.  Separating objects and properties by their atomic meanings provides several advantages.

- Reduce errors in software and database development by ensuring that data is consistent and valid.
- Increase consistency in documentation and system design by using common terms, patterns, and standards.
- Improve application and database performance by minimizing data redundancy and optimizing data structures.
- Ease data mapping and improve communication between data providers and consumers.

## Extensible
Extensibility is the ability to add capabilities without rewriting code or changing the basic architecture.   Extensibility allows users and their software systems to quickly adapt to dynamic market and technology conditions.  The AKM is designed so that users can extend the schema with new classes, objects, properties, and attributes without breaking existing code.  Generally useful extensions can be submitted to the repository for review and acceptance. 

Some ways that AKM provides extensibility are:
- The model eschews enumerations in favor of explicit objects.  Instead of an enumeration of data types, for instance, the model defines a DataType class whose members are stored as json objects.
- The model discourages the use of discrete identifiers (sometimes called "magic numbers").  For instance, rather than encode metric information in a field value as *Vehicle.Speed.KilometerPerHour.UInt8*, the metric explicitly articulates that information as *featureOfinterest: VehicleTravel, property: Speed, Unit: kilometer_per_hour*, and *dataType: uint8*.
- Custom extensions are ignored by any validation or tools provided in the public repository.
- The information is expressive and articulate enough to support the inference and automation enabled by formal knowledge systems like ontologies.

## Standardized
Standards allow information to flow seamlessly between systems and organizations.  AKM is designed to promote internal consistency by providing a well-defined set of objects that represent vehicle metrics.  
### Internal Standards
AKM employs standards to ensure its quality and consistency.

- Objects inherit from a standard ***Entity*** that defines common properties such as name, definition, comment, etc.
- All objects and properties fields include their definition using the JSON Schema ***description*** keyword.
### External Standards
AKM is also designed to utilize external standards.
#### Standard Schema Language
[JSON Schema](https://json-schema.org/)  is a well-known vocabulary that enables JSON data consistency, validity, and interoperability at scale.
#### Common Terms and Vocabularies
AKM tries to appropriate established terms where possible, and its main classes provide an example:
- **Feature of Interest** is a common term in IoT vocabularies, including:
 >- [SOSA](https://www.w3.org/TR/vocab-ssn/) - the Sensor, Observation, Sample, and Actuator Ontology
 >- [SAREF](https://saref.etsi.org/core/v3.1.1/) - the Smart Applications REFerence ontology
 >- The [OGC SensorThings API](https://www.ogc.org/standard/sensorthings/)
 >
- **Property** is a term used in many programming languages to indicate an attribute that can be observed (read) or manipulated (written).
- **Metric** is a common business intelligence term to indicate something that is measured but doesn't include the measurements themselves.

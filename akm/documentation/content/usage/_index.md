---
title: Usage Guidelines
weight: 40
chapter: true
---

# Usage Guidelines

## Partition Things / Reuse Properties
Favor partitioning features of interest into their components rather than creating bespoke properties.  For example, use this:
```
Vehicle.Seat.Row1.Left.IsOccupied
Vehicle.Seat.Row1.Right.IsOccupied
```
...rather than this:
```
Vehicle.Seat.IsRow1LeftOccupied
Vehicle.Seat.IsRow1RightOccupied
```
This allows the property (*IsOccupied* in this example) to be defined once, providing a specific and consistent meaning.  Also, models attain resilience when they represent reality. There is, in fact, a seat at the front left and front right.  Those instances may acquire new properties. For example:
```
Vehicle.Seat.Row1.Left.FabricType
Vehicle.Seat.Row1.Left.IsHeated
```

## Treat Metrics as Optional
The current customary practice is to assign a unique identifier to every metric.  In other words, every combination of feature of interest and property has its own identifier.  This is analogous to the retail industry where every combination of size and color for a tee shirt has a unique stockkeeping unit (SKU).  The retail industry requires this because they maintain inventory and order stock from several suppliers and require a system that works with all their items.  

Automotive information doesn't have those constraints.  It's just digital information for which there is no inventory or resupply needs.  There is an opportunity to use the more flexible approach used by taquerias, who would be crazy to offer a menu item for every combination of meat, rice, beans, and vegetable that a burrito could contain.  Instead, the customer orders a burrito, and then selects from a list of ingredients.

Some systems would only need to maintain the sum of features of interest and properties:
 ```YAML
FeatureOfInterest: Vehicle.Seat.Row1.Left
FeatureOfInterest: Vehicle.Seat.Row1.Right
FeatureOfInterest: Vehicle.Seat.Row2.Left
FeatureOfInterest: Vehicle.Seat.Row2.Right

Property: IsOccupied
Property: IsHeated
Property: FabricType
```
...rather than all possible combinations:
```
Vehicle.Seat.Row1.Left.IsOccupied
Vehicle.Seat.Row1.Right.IsOccupied
Vehicle.Seat.Row2.Left.IsOccupied
Vehicle.Seat.Row2.Right.IsOccupied

Vehicle.Seat.Row1.Left.FabricType
Vehicle.Seat.Row1.Right.FabricType
Vehicle.Seat.Row2.Left.FabricType
Vehicle.Seat.Row2.Right.FabricType

Vehicle.Seat.Row1.Left.IsHeated
Vehicle.Seat.Row1.Right.IsHeated
Vehicle.Seat.Row2.Left.IsHeated
Vehicle.Seat.Row2.Right.IsHeated
```
The detail moves to the payload of a generic metric object:
 ```YAML
Metric:
  featureOfInterest: Vehicle.Seat.Row1.Left
  property: IsOccupied
  value: true
```
This lays the foundation for an even more compact model:
 ```YAML
FeatureOfInterest: Vehicle.Seat

Property: IsOccupied
Property: IsHeated
Property: FabricType
Property: Row
Property: LateralPosition
```
...in which metrics can identify specific instances:
 ```YAML
Metric:
  featureOfInterest: Vehicle.Seat
  row: 1
  lateralPosition: Left
  property: IsOccupied
  value: true
 ```
This is not meant to say that Metrics ***are*** optional.   There are automotive standards for CAN bus and diagnostic codes that will stay embedded for some time.  It may also be useful to explicitly declare which properties apply to which features of interest for enabling such things as authorization and privacy policies.  The point is that conceiving of metrics as optional prepares for a future that eases the maintenance of vehicle metadata and allows the metadata to be understood and acted on by machines and algorithms.




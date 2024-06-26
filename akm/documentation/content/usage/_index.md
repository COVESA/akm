
---
title: Usage Guidelines
weight: 40
chapter: true
---

# Usage Guidelines

## Partition Things / Reuse Properties
Favor partitioning features of interest into their components rather than creating bespoke properties.  For example, use this:
```
Seat.Row1.Left.IsOccupied
Seat.Row1.Right.IsOccupied
```
...rather than this:
```
Seat.Is_Row1_Left_Occupied
Seat.Is_Row1_Right_Occupied
```
This allows the property (*IsOccupied* in this example) to be defined once, providing a specific and consistent meaning.  Also, models attain resilience when they represent reality. There is, in fact, a seat at the front left and front right.  Those instances may acquire new properties. For example:
```
Seat.Row1.Left.FabricType
Seat.Row1.Left.IsHeated
```

## Treat Signal Definitions as Optional
The current customary practice is to assign a unique identifier to every signal.  For metrics, every combination of feature of interest and property has its own identifier.  This is analogous to the retail industry where every combination of size and color for a tee shirt has a unique stockkeeping unit (SKU).  The retail industry requires this because they maintain inventory and order stock from several suppliers and require a system that works with all their items.  

Automotive information doesn't have those constraints.  It's just digital information for which there is no inventory or resupply needs.  There is an opportunity to use the more flexible approach used by taquerias, who would be crazy to offer a menu item for every combination of meat, rice, beans, and vegetable that a burrito could contain.  Instead, the customer orders a burrito, and then selects from a list of ingredients.

Systems would only need to maintain the sum of features of interest and properties:
 ```YAML
FeatureOfInterest: Seat.Row1.Left
FeatureOfInterest: Seat.Row1.Right
FeatureOfInterest: Seat.Row2.Left
FeatureOfInterest: Seat.Row2.Right

Property: IsOccupied
Property: IsHeated
Property: FabricType
```
...rather than the product:
```
Seat.Row1.Left.IsOccupied
Seat.Row1.Right.IsOccupied
Seat.Row2.Left.IsOccupied
Seat.Row2.Right.IsOccupied

Seat.Row1.Left.FabricType
Seat.Row1.Right.FabricType
Seat.Row2.Left.FabricType
Seat.Row2.Right.FabricType

Seat.Row1.Left.IsHeated
Seat.Row1.Right.IsHeated
Seat.Row2.Left.IsHeated
Seat.Row2.Right.IsHeated
```
The detail moves to the payload of a generic metric object:
 ```YAML
Metric:
  featureOfInterest: Seat.Row1.Left
  property: IsOccupied
  value: true
```
This lays the foundation for an even more compact model:
 ```YAML
FeatureOfInterest: Seat

Property: IsOccupied
Property: IsHeated
Property: FabricType
Property: CabinRow
Property: LateralPosition
```
...in which metrics can identify specific instances when needed:
 ```YAML
Metric:
  featureOfInterest: Seat
  cabinRow: 1
  lateralPosition: Left
  property: IsOccupied
  value: true
 ```
This is not meant to say that Metrics ***are*** optional.   There are automotive standards for CAN bus and diagnostic codes that will stay embedded for some time.  It may also be useful to explicitly declare which properties apply to which features of interest for enabling such things as authorization and privacy policies.  The point is that conceiving of metrics as optional prepares for a future that eases the maintenance of vehicle metadata and allows the metadata to be understood and acted on by machines and algorithms.

---
title: Overlays
weight: 50
chapter: true
---

# Overlays
Overlays are used to add and/or extend the content to the akm. 
The purpose of overlay feature is to enable suppliers and OEMs to be able to add and/or extend
the existing entities such as FeatureOfInterest, Metrics, Properties, datatypes, units etc. 

Note: It is NOT allowed to use overlays to redefine or override existing definetions in base akm data folder.


## Location and folder structure
To add any overlays one can use existing default folder named "overlays" under the "akm" folder 
or can create a new folder outside akm folder. This folder needs to have the same subfolders as "data", specifically: 
- feature_of_interest
- metric
- property
- reference

## Add content
### Feature -> Feature of Interest
For each feature (e.g. traction battery) a new .json file shall be added to the "overlays/feature_of_interest" folder. The newly added FOI file shall contain the representation of "physical" things according to the specification for FOI (e.g. the traction battery itself, the contactor of the battery, the DCDC converter etc.). 

### Metrics 
The relevant metrics for the newly added FOI are added in separate files in the "overlays/metrics" folder. Please consider meaningful filenames (e.g. metrics-TractionBattery.json). 

### Properties 
The required properties (data- and/or objectproperties) are added to the "overlays/property" folder. 
For data properties (e.g. the number of cells in the traction battery), the content shall be added to the "data_properties.json" file in the "overlays/property" folder. 
Object properties (e.g. the contactor state of the battery)shall be added to the file "object_properties.json" respectively. 

### Data types and units
If the newly added content has unknown units and/or datatypes, the corresponding information shall be added to the files "overlays/reference/datatypes.json" and "overlays/reference/units.json". 

### Hint 
The author is advised to check the “akm/data” folders first if the needed properties already exist (e.g. temperature). General advice: Reuse as much as possible! Especially for units/datatypes, the information is very likely already present in the "akm/data/reference" folder. 

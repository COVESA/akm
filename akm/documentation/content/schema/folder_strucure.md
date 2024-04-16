
---
title: Folder Structure
weight: 3
---

There are three main folders:

- **\schema** contains the JSON Schema file(s) that provide the structure and meaning of the automotive metadata files

- **\data** contains the JSON documents that contain the actual Automotive metadata

- **\documentation** contains markdown files that explain aspects of the AKM, Content can be used for document generation using Hugo.


Within the *data* folder, the AKM allows the following to be modified at will ***with no effect on validation, tooling, or other processes***:
- the organization of folders and files within the tree
- the names of folders and files
- the inclusion of entries in each json file

The initial release of the data folder contains sample data files and a subfolder for reference data.

The repo is currently in an alpha release state and should be considered a **DRAFT**.  

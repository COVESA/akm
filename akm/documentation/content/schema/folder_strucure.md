---
title: Folder Structure of AKM
weight: 3
---


The AKM Folder conatins four subfolders:

- **\schema** contains the JSON Schema file(s) that provide the structure and meaning of the automotive metadata files

- **\data** contains the JSON documents that contain the actual Automotive metadata

- **\documentation** contains markdown files that explain aspects of the AKM, Content can be used for document generation using Hugo.

- **\rdf** contains a turtle file that expresses the structure and metadata in an ontology

The repo is currently in an alpha release state and should be considered a **DRAFT**.  
It requires the following work to make it generally available:

- The format and structure of the JSON Schema document requires testing, restructuring, and other quality reviews.
- The tooling that converts VSS to other formats must be available to the AKM.  (The AKM tools should be simpler because of the many existing JSON Schema libraries, tooling, etc.)
- The processing of VSS overlays should be supported.
- An assessment of how exposing a DAG that is not necessarily the VSS tree would affect the [VISS](https://www.w3.org/TR/viss2-core/).
- The structure of the data subfolders should be appraised.
- The generation of JSON data documents from RDF and vice versa should be developed.

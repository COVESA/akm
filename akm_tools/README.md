# AKM Tools 

This project provides a set of tools for parsing, validating, and exporting Automotive Knowledge Model (AKM) data. It supports handling JSON files from specified directories, validating them against given schemas, and exporting the validated data into different formats including JSON and YAML. The functionality is encapsulated into a Python script that can be executed from the command line, offering flexibility for automation and integration into larger systems or workflows.

## Features

- **Data Validation**: Validate the combined data against a provided schema and optional extended schemas.
- **Data Exporting**: Export the validated data into various formats such as JSON and YAML. Support for GraphQL export is planned but not yet implemented.


## Usage

The main functionality is accessed through the command line interface (CLI) provided by `akm_parser.py`. Below are the available options and their descriptions:

### Command Line Arguments

- `-d`, `--model_data_folder`: Specifies the directory containing AKM model data in JSON format. Default is `akm/data`.
- `-s`, `--schema`: Specifies the schema file against which the data will be validated. Default is `akm/schema/automotive_knowledge_model.json`.
- `-xs`, `--extended_schema_dir`: Specifies the directory containing extended schema files for validation. Default is `extensions/schema`.
- `-xd`, `--extended_data_dir`: Specifies the directory containing extended data. Default is `extensions/data`.

- `-e`, `--export_format`: Specifies the format for exporting validated data. Options are `json`, `yaml`
- `-f`, `--export_file_path`: Specifies the path for the export file. Required if `--export_format` is specified.

### Example Commands

Validate data without exporting:
```
python akm_tools/akm_parser.py -xd your_extended_data_folder
```

Export validated data to JSON:
```
python akm_tools/akm_parser.py -d your_model_data_folder -e json -f path/to/export.json
```
### Logging
Validation errors are logged to validation_errors.log, aiding in troubleshooting and ensuring data quality.
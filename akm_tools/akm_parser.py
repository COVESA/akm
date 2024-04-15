import os
import json
import argparse
from pprint import pprint as pp
from akm_tools.validation import AKMDataValidator
from akm_tools.utils import YamlCustomDumper


def parse_data_from_file(file_name):
    with open(file_name, "r") as f:
        data = json.load(f)
    return data


def create_and_combine_json_from_a_folder(dir_path):
    list_to_return = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith(".json"):
                file_path = os.path.join(root, file)
                list_to_return = list_to_return + parse_data_from_file(file_path)
    return list_to_return


def parse_and_validate_data(model_folder, schema, extended_schema_dir, overlays):
    model_data_list = create_and_combine_json_from_a_folder(model_folder)
    overlay_data_list = create_and_combine_json_from_a_folder(overlays)
    all_data = model_data_list + overlay_data_list
    validator_object = AKMDataValidator(schema=schema)
    validated_model_data = validator_object.validate_data_instances(all_data, extended_schema_dir=extended_schema_dir)
    validated_model_data = validator_object.validate_contexts(all_data=validated_model_data)  ## passing valid instances
    validator_object.log_errors()

    return validated_model_data


def export_to_json(validated_model_data, file_name):
    with open(file_name, "w") as fw:
        fw.write(json.dumps(validated_model_data, indent=4))


def export_to_yaml(validated_model_data, file_name):
    with open(file_name, "w") as fw:
        fw.write(YamlCustomDumper.dumps(validated_model_data))


# def export_to_graphql(validated_model_data, file_name):
#     print("to be implemented")


def main():
    # Mapping of format choices to their corresponding functions
    export_functions = {
        "json": export_to_json,
        "yaml": export_to_yaml,
        # "graphql": export_to_graphql,
    }

    parser = argparse.ArgumentParser(description="Parse, validate, and optionally export AKM data.")
    ## optional
    parser.add_argument(
        "-d",
        "--model_data_folder",
        type=str,
        default="akm/data",
        help="AKM model data folder",
    )
    parser.add_argument(
        "-s",
        "--schema",
        type=str,
        default="akm/schema/automotive_knowledge_model.json",
        help="AKM schema file",
    )
    parser.add_argument(
        "-xs",
        "--extended_schema_dir",
        type=str,
        default="extensions/schema",
        help="Directory for extended schema files",
    )
    parser.add_argument(
        "-xd",
        "--extended_data_dir",
        type=str,
        default="extensions/data",
        help="Directory for extended data",
    )
    ## export options
    parser.add_argument(
        "-e",
        "--export_format",
        type=str,
        choices=export_functions.keys(),
        help="Specifies the export format",
    )
    parser.add_argument("-f", "--export_file_path", type=str, help="Path for export file")
    args = parser.parse_args()

    if args.export_format and not args.export_file_path:
        parser.error("--export requires --format to be specified. Choose either 'json' or 'yaml'.")

    with open(args.schema, "r") as f:
        schema = json.load(f)
    validated_model_data = parse_and_validate_data(
        args.model_data_folder, schema, args.extended_schema_dir, args.extended_data_dir
    )

    if args.export_format:
        export_functions[args.export_format](validated_model_data, args.export_file_path)
    else:
        print("Export not requested. Validation complete.")


if __name__ == "__main__":
    main()

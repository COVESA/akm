import logging
from typing import Dict, List

from .data_instance_validators import CoreJsonSchemaValidator
from .data_context_validators import ExtendedInstanceContentValidator, CrossReferenceValidator

# Set up logging
logging.basicConfig(
    filename="validation_errors.log",
    level=logging.INFO,
    format="%(message)s",
    filemode="w",
)


# Validation Orchestrator Class
class AKMDataValidator:
    def __init__(
        self,
        schema,
        data_instance_validators=[CoreJsonSchemaValidator],
        complete_data_context_validators=[ExtendedInstanceContentValidator, CrossReferenceValidator],
    ):
        self.schema = schema
        self.data_instance_validators_class_list = data_instance_validators
        self.complete_data_validators_class_list = complete_data_context_validators
        self.validation_errors = []
        self.extended_schema_dir = None

    def validate_data_instances(self, all_data: List[Dict], **kwargs):
        print("Validating Data Instances")
        if "extended_schema_dir" in kwargs.keys():
            self.extended_schema_dir = kwargs["extended_schema_dir"]
        ## configure data_instance_validator_objects
        data_instance_validator_objects = self._configure_data_instance_validators()
        valid_data = []
        for instance in all_data:
            for instance_validator in data_instance_validator_objects:
                valid, error_msg = instance_validator.validate(instance=instance)
                if valid:
                    valid_data.append(instance)
                else:
                    self.validation_errors.append(error_msg)
        return valid_data

    def _configure_data_instance_validators(self):
        data_instance_validator_objects = [
            obj(schema=self.schema, extended_schema_dir=self.extended_schema_dir)
            for obj in self.data_instance_validators_class_list
        ]
        return data_instance_validator_objects

    def log_errors(self):
        for error_msg in self.validation_errors:
            logging.error(error_msg)

    def validate_contexts(self, all_data: List[Dict]):
        print("Validating Data Contexts")
        # Perform cross-reference validation if the cross-reference validator is included
        valid_data = all_data
        for context_validator in self.complete_data_validators_class_list:
            context_validator_object = context_validator()
            valid_data = context_validator_object.validate_data_contexts(valid_data)
            self.validation_errors = self.validation_errors + context_validator_object.error_messages
        return valid_data

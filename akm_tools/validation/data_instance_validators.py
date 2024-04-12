from abc import ABC, abstractmethod
from typing import Dict, List, Any, Optional
from referencing import Registry
from referencing.jsonschema import DRAFT202012
from pathlib import Path
import json
from jsonschema.exceptions import ValidationError
from jsonschema import Draft202012Validator
from .global_debug_config import GlobalDebugConfig


class DataInstanceValidator(ABC):
    """
    Base Instance Validator Interface
    Use this for adding more Instance level Validator Classes
    """

    @abstractmethod
    def validate(self, instance: dict, **kwargs):
        pass


# Concrete Validator Implementations
class CoreJsonSchemaValidator:
    def __init__(self, schema: Dict, extended_schema_dir: Optional[str]):
        self.schema = schema
        self.registry = None
        self.main_validator = None
        self.object_validators_dict = None
        self.extended_schema_dir = extended_schema_dir
        self._configure_registry_and_validators()

    def _configure_registry_and_validators(self):
        self.registry = self._create_registry()
        self._configure_validators()

    def _create_registry(self) -> Registry:
        """Configure and return a registry with all schemas."""
        extension_schema_registry_entries = [(self.schema["$id"], DRAFT202012.create_resource(self.schema))]

        if self.extended_schema_dir:
            path_extended_schema_dir = Path(self.extended_schema_dir)
            try:
                extended_schemas_list = [json.load(x.open()) for x in path_extended_schema_dir.glob("*.json")]
                object_schema_registry_entries = [(x["$id"], DRAFT202012.create_resource(x)) for x in extended_schemas_list]
                extension_schema_registry_entries += object_schema_registry_entries
            except (IOError, json.JSONDecodeError) as e:
                print(f"Error processing extended schemas: {e}")

        return Registry().with_resources(extension_schema_registry_entries)

    def configure_registry(self, registry: Registry):
        self.registry = registry
        self._configure_validators()

    def _configure_validators(self):
        self.object_validators_dict = self._create_individual_object_validators()
        self.main_validator = self._create_main_validator()

    def _create_main_validator(self):
        return Draft202012Validator(self.schema, registry=self.registry)

    def _create_individual_object_validators(self) -> Dict[str, any]:
        validators = {}
        if "$defs" in self.schema:
            for key, schema_def in self.schema["$defs"].items():
                validators[key] = Draft202012Validator(schema_def, registry=self.registry)
        return validators

    def validate(self, instance: dict, **kwargs):
        try:
            self.main_validator.validate(instance=instance)
            return True, ""
        except ValidationError as e:
            if GlobalDebugConfig.debug_mode:
                raise e
            else:
                ## main validator Failed
                base_error_msg = f"Validation Error for {(e.message)}\n"
                if "entityTypeID" in instance.keys():
                    if instance["entityTypeID"] in self.object_validators_dict.keys():
                        additioanl_error_info = sorted(
                            self.object_validators_dict[instance["entityTypeID"]].iter_errors(instance),
                            key=lambda e: e.path,
                        )
                    base_error_msg += "\n".join(x.message for x in additioanl_error_info)
                    base_error_msg += "\n"
                return False, base_error_msg
        except Exception as e:
            raise e

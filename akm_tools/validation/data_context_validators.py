from abc import ABC, abstractmethod
from typing import Dict, List, Any
from .global_debug_config import GlobalDebugConfig
from .custom_exceptions import IDConflictException, BaseInstanceOverwiteException, InvalidReferentIDException


class AllDataContextValidators(ABC):
    """
    Base Complete Data References/Context Validator Interface
    These type of validators work on the context of all the data together, instead of just one instance
    """

    error_messages = []

    @abstractmethod
    def validate_data_contexts(self, all_data: List[Dict[str, Any]]):
        pass

    @classmethod
    def create_instance_dict(self, all_data):
        # Populate the instance_dict dictionary
        instance_dict = {}
        for instance in all_data:
            if "id" in instance:
                instance_id = instance["id"]
                if instance_id not in instance_dict:
                    # Initialize the ID key with a list containing the current instance
                    instance_dict[instance_id] = {"count": 1, "instances": [instance]}
                else:
                    # Append the current instance to the list and increment the count
                    instance_dict[instance_id]["instances"].append(instance)
                    instance_dict[instance_id]["count"] += 1
        return instance_dict

    def _handle_error(self, exception_type, *args):
        error_exception = exception_type(*args)
        if GlobalDebugConfig.debug_mode:
            raise error_exception
        else:
            self.error_messages.append(error_exception.message)


class ExtendedInstanceContentValidator(AllDataContextValidators):
    """
    For Instances with duplicate "id", where one extends the other,
    check if the extended Instance does not overwrite content of base instance
    """

    def __init__(self):
        self.warning_messages = []

    def validate_data_contexts(self, all_data: List[Dict[str, Any]]):
        valid_data = []
        instance_dict = self.__class__.create_instance_dict(all_data)

        # Handle instances with same ids and prepare valid_data
        for instance_id, instance_content in instance_dict.items():
            if len(instance_content) > 2:
                self._handle_multiple_id_conflicts(instance_content)
            if instance_content["count"] == 2:
                # check if the insances are not overriding , but only extending existing data.
                is_valid_extension, base_instance, extended_instance = self.__class__.check_data_is_extended_not_overwritten(
                    instance_content["instances"]
                )
                if is_valid_extension:
                    valid_data.append(extended_instance)
                    self.warning_messages.append(
                        f"Base instance will be ignored. :\n{base_instance}\nwas extended by \n{extended_instance}"
                    )
                else:
                    valid_data.append(base_instance)
                    self._handle_extension_overwrite(base_instance, extended_instance)
            else:
                valid_data.append(instance_content["instances"][0])  ## there should be only one entry
        return valid_data

    @classmethod
    def check_data_is_extended_not_overwritten(self, instances: List[Dict]):
        # Determine which instance is the base and which is the extension
        instance1, instance2 = instances[0], instances[1]
        base_instance, extended_instance = (
            (instance1, instance2) if len(instance1) <= len(instance2) else (instance2, instance1)
        )
        # Check every property in the base instance to see if it exists in the extended instance
        # with the same value
        for key, value in base_instance.items():
            if key not in extended_instance or extended_instance[key] != value:
                return False, base_instance, extended_instance
        return True, base_instance, extended_instance

    def _handle_multiple_id_conflicts(self, instances: List[Dict]):
        self._handle_error(IDConflictException, instances)

    def _handle_extension_overwrite(self, base_instance, extended_instance):
        self._handle_error(BaseInstanceOverwiteException, base_instance, extended_instance)


class CrossReferenceValidator(AllDataContextValidators):
    def __init__(self):
        self.id_set = set()

    def validate_data_contexts(self, all_data):
        # Create a dictionary mapping IDs to data instances
        id_to_instance = {instance["id"]: instance for instance in all_data if "id" in instance}

        # Create a dictionary mapping IDs to their validity
        id_to_validity = {id: None for id in id_to_instance}

        def is_valid(id):
            # If the ID is not in the dictionary, it's invalid
            if id not in id_to_instance:
                return False

            # If the validity has already been determined, return it
            if id_to_validity[id] is not None:
                return id_to_validity[id]

            # Mark the ID as being checked to handle circular references
            id_to_validity[id] = False

            instance = id_to_instance[id]
            for key, value in instance.items():
                if (
                    isinstance(value, dict)
                    and "referentEntityTypeID" in value  ## this is hard dependency to schema for akm.Reference
                    and "referentID" in value
                ):
                    if not is_valid(value["referentID"]):
                        return False

            # If all references are valid, the instance is valid
            id_to_validity[id] = True
            return True

        # Validate the references
        for id in id_to_instance:
            is_valid(id)

        # Collect the valid data
        valid_data = [instance for id, instance in id_to_instance.items() if id_to_validity[id]]

        return valid_data

    def _handle_extension_overwrite(self, instance, referentID_value):
        self._handle_error(InvalidReferentIDException, instance, referentID_value)

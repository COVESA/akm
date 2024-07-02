from typing import Dict, List
from deepdiff import DeepDiff
import json

class IDConflictException(Exception):
    def __init__(self, instances: List[Dict]):
        err_msg = f"More than 2 instances with same  ID ! \n{json.dumps(instances,indent=2)}\n"
        super().__init__(err_msg)
        self.message = err_msg


class BaseInstanceOverwiteException(Exception):
    def __init__(self, base_instance: dict, extended_instance: dict):
        diff = DeepDiff(base_instance, extended_instance, ignore_order=True)
        err_msg = (
            f"Issue with {base_instance['id']}\nThe extended instance is overwriting properties of base instance:\n{diff.pretty()}\n"
        )
        super().__init__(err_msg)
        self.message = err_msg


class InvalidReferentIDException(Exception):
    def __init__(self, instance : dict, referentID):
        err_msg = f"The instance :\n{json.dumps(instance,indent=2)}\nis referencing an invalid id : '{referentID}'\n"
        super().__init__(err_msg)
        self.message = err_msg

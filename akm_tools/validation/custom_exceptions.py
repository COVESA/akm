from typing import Dict, List


class IDConflictException(Exception):
    def __init__(self, instances: List[Dict]):
        err_msg = f"More than 2 instances with same  ID ! \n{instances}\n"
        super().__init__(err_msg)
        self.message = err_msg


class BaseInstanceOverwiteException(Exception):
    def __init__(self, base_instance, extended_instance):
        err_msg = (
            f"The extended instance :\n{extended_instance}\nis overwriting properties of base instance\n{base_instance}\n"
        )
        super().__init__(err_msg)
        self.message = err_msg


class InvalidReferentIDException(Exception):
    def __init__(self, instance, referentID):
        err_msg = f"The instance :\n{instance}\nis referencing an invalid id : '{referentID}'\n"
        super().__init__(err_msg)
        self.message = err_msg

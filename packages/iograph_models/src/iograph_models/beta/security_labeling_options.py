from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityLabelingOptions(BaseModel):
	assignmentMethod: Optional[SecurityAssignmentMethod | str] = Field(alias="assignmentMethod", default=None,)
	downgradeJustification: Optional[SecurityDowngradeJustification] = Field(alias="downgradeJustification", default=None,)
	extendedProperties: Optional[list[SecurityKeyValuePair]] = Field(alias="extendedProperties", default=None,)
	labelId: Optional[str] = Field(alias="labelId", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .security_assignment_method import SecurityAssignmentMethod
from .security_downgrade_justification import SecurityDowngradeJustification
from .security_key_value_pair import SecurityKeyValuePair


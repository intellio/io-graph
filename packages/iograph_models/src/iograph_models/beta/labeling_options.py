from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class LabelingOptions(BaseModel):
	assignmentMethod: Optional[AssignmentMethod | str] = Field(alias="assignmentMethod", default=None,)
	downgradeJustification: Optional[DowngradeJustification] = Field(alias="downgradeJustification", default=None,)
	extendedProperties: Optional[list[KeyValuePair]] = Field(alias="extendedProperties", default=None,)
	labelId: Optional[str] = Field(alias="labelId", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .assignment_method import AssignmentMethod
from .downgrade_justification import DowngradeJustification
from .key_value_pair import KeyValuePair


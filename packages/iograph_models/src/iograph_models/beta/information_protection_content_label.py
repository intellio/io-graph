from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class InformationProtectionContentLabel(BaseModel):
	assignmentMethod: Optional[AssignmentMethod | str] = Field(alias="assignmentMethod", default=None,)
	creationDateTime: Optional[datetime] = Field(alias="creationDateTime", default=None,)
	label: Optional[LabelDetails] = Field(alias="label", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .assignment_method import AssignmentMethod
from .label_details import LabelDetails

from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SensitivityLabelAssignment(BaseModel):
	assignmentMethod: Optional[SensitivityLabelAssignmentMethod | str] = Field(alias="assignmentMethod",default=None,)
	sensitivityLabelId: Optional[str] = Field(alias="sensitivityLabelId",default=None,)
	tenantId: Optional[str] = Field(alias="tenantId",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .sensitivity_label_assignment_method import SensitivityLabelAssignmentMethod


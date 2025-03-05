from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SensitivityLabelAssignment(BaseModel):
	assignmentMethod: Optional[SensitivityLabelAssignmentMethod] = Field(default=None,alias="assignmentMethod",)
	sensitivityLabelId: Optional[str] = Field(default=None,alias="sensitivityLabelId",)
	tenantId: Optional[str] = Field(default=None,alias="tenantId",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .sensitivity_label_assignment_method import SensitivityLabelAssignmentMethod


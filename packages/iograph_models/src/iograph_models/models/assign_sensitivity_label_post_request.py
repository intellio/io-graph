from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Assign_sensitivity_labelPostRequest(BaseModel):
	sensitivityLabelId: Optional[str] = Field(default=None,alias="sensitivityLabelId",)
	assignmentMethod: Optional[SensitivityLabelAssignmentMethod] = Field(default=None,alias="assignmentMethod",)
	justificationText: Optional[str] = Field(default=None,alias="justificationText",)

from .sensitivity_label_assignment_method import SensitivityLabelAssignmentMethod


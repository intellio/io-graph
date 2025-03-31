from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Assign_sensitivity_labelPostRequest(BaseModel):
	sensitivityLabelId: Optional[str] = Field(alias="sensitivityLabelId", default=None,)
	assignmentMethod: Optional[SensitivityLabelAssignmentMethod | str] = Field(alias="assignmentMethod", default=None,)
	justificationText: Optional[str] = Field(alias="justificationText", default=None,)

from .sensitivity_label_assignment_method import SensitivityLabelAssignmentMethod

from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AssignmentFilterTypeAndEvaluationResult(BaseModel):
	assignmentFilterType: Optional[DeviceAndAppManagementAssignmentFilterType | str] = Field(alias="assignmentFilterType",default=None,)
	evaluationResult: Optional[AssignmentFilterEvaluationResult | str] = Field(alias="evaluationResult",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .device_and_app_management_assignment_filter_type import DeviceAndAppManagementAssignmentFilterType
from .assignment_filter_evaluation_result import AssignmentFilterEvaluationResult


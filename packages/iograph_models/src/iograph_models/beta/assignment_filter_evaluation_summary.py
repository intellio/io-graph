from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AssignmentFilterEvaluationSummary(BaseModel):
	assignmentFilterDisplayName: Optional[str] = Field(alias="assignmentFilterDisplayName", default=None,)
	assignmentFilterId: Optional[str] = Field(alias="assignmentFilterId", default=None,)
	assignmentFilterLastModifiedDateTime: Optional[datetime] = Field(alias="assignmentFilterLastModifiedDateTime", default=None,)
	assignmentFilterPlatform: Optional[DevicePlatformType | str] = Field(alias="assignmentFilterPlatform", default=None,)
	assignmentFilterType: Optional[DeviceAndAppManagementAssignmentFilterType | str] = Field(alias="assignmentFilterType", default=None,)
	assignmentFilterTypeAndEvaluationResults: Optional[list[AssignmentFilterTypeAndEvaluationResult]] = Field(alias="assignmentFilterTypeAndEvaluationResults", default=None,)
	evaluationDateTime: Optional[datetime] = Field(alias="evaluationDateTime", default=None,)
	evaluationResult: Optional[AssignmentFilterEvaluationResult | str] = Field(alias="evaluationResult", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .device_platform_type import DevicePlatformType
from .device_and_app_management_assignment_filter_type import DeviceAndAppManagementAssignmentFilterType
from .assignment_filter_type_and_evaluation_result import AssignmentFilterTypeAndEvaluationResult
from .assignment_filter_evaluation_result import AssignmentFilterEvaluationResult


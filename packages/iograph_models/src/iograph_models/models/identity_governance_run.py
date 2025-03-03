from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class IdentityGovernanceRun(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	completedDateTime: Optional[datetime] = Field(default=None,alias="completedDateTime",)
	failedTasksCount: Optional[int] = Field(default=None,alias="failedTasksCount",)
	failedUsersCount: Optional[int] = Field(default=None,alias="failedUsersCount",)
	lastUpdatedDateTime: Optional[datetime] = Field(default=None,alias="lastUpdatedDateTime",)
	processingStatus: Optional[IdentityGovernanceLifecycleWorkflowProcessingStatus] = Field(default=None,alias="processingStatus",)
	scheduledDateTime: Optional[datetime] = Field(default=None,alias="scheduledDateTime",)
	startedDateTime: Optional[datetime] = Field(default=None,alias="startedDateTime",)
	successfulUsersCount: Optional[int] = Field(default=None,alias="successfulUsersCount",)
	totalTasksCount: Optional[int] = Field(default=None,alias="totalTasksCount",)
	totalUnprocessedTasksCount: Optional[int] = Field(default=None,alias="totalUnprocessedTasksCount",)
	totalUsersCount: Optional[int] = Field(default=None,alias="totalUsersCount",)
	workflowExecutionType: Optional[IdentityGovernanceWorkflowExecutionType] = Field(default=None,alias="workflowExecutionType",)
	taskProcessingResults: Optional[list[IdentityGovernanceTaskProcessingResult]] = Field(default=None,alias="taskProcessingResults",)
	userProcessingResults: Optional[list[IdentityGovernanceUserProcessingResult]] = Field(default=None,alias="userProcessingResults",)

from .identity_governance_lifecycle_workflow_processing_status import IdentityGovernanceLifecycleWorkflowProcessingStatus
from .identity_governance_workflow_execution_type import IdentityGovernanceWorkflowExecutionType
from .identity_governance_task_processing_result import IdentityGovernanceTaskProcessingResult
from .identity_governance_user_processing_result import IdentityGovernanceUserProcessingResult


from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class IdentityGovernanceUserProcessingResult(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	completedDateTime: Optional[datetime] = Field(default=None,alias="completedDateTime",)
	failedTasksCount: Optional[int] = Field(default=None,alias="failedTasksCount",)
	processingStatus: Optional[IdentityGovernanceLifecycleWorkflowProcessingStatus] = Field(default=None,alias="processingStatus",)
	scheduledDateTime: Optional[datetime] = Field(default=None,alias="scheduledDateTime",)
	startedDateTime: Optional[datetime] = Field(default=None,alias="startedDateTime",)
	totalTasksCount: Optional[int] = Field(default=None,alias="totalTasksCount",)
	totalUnprocessedTasksCount: Optional[int] = Field(default=None,alias="totalUnprocessedTasksCount",)
	workflowExecutionType: Optional[IdentityGovernanceWorkflowExecutionType] = Field(default=None,alias="workflowExecutionType",)
	workflowVersion: Optional[int] = Field(default=None,alias="workflowVersion",)
	subject: Optional[User] = Field(default=None,alias="subject",)
	taskProcessingResults: list[IdentityGovernanceTaskProcessingResult] = Field(alias="taskProcessingResults",)

from .identity_governance_lifecycle_workflow_processing_status import IdentityGovernanceLifecycleWorkflowProcessingStatus
from .identity_governance_workflow_execution_type import IdentityGovernanceWorkflowExecutionType
from .user import User
from .identity_governance_task_processing_result import IdentityGovernanceTaskProcessingResult


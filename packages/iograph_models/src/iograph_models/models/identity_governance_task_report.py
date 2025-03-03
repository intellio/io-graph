from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class IdentityGovernanceTaskReport(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	completedDateTime: Optional[datetime] = Field(default=None,alias="completedDateTime",)
	failedUsersCount: Optional[int] = Field(default=None,alias="failedUsersCount",)
	lastUpdatedDateTime: Optional[datetime] = Field(default=None,alias="lastUpdatedDateTime",)
	processingStatus: Optional[IdentityGovernanceLifecycleWorkflowProcessingStatus] = Field(default=None,alias="processingStatus",)
	runId: Optional[str] = Field(default=None,alias="runId",)
	startedDateTime: Optional[datetime] = Field(default=None,alias="startedDateTime",)
	successfulUsersCount: Optional[int] = Field(default=None,alias="successfulUsersCount",)
	totalUsersCount: Optional[int] = Field(default=None,alias="totalUsersCount",)
	unprocessedUsersCount: Optional[int] = Field(default=None,alias="unprocessedUsersCount",)
	task: Optional[IdentityGovernanceTask] = Field(default=None,alias="task",)
	taskDefinition: Optional[IdentityGovernanceTaskDefinition] = Field(default=None,alias="taskDefinition",)
	taskProcessingResults: Optional[list[IdentityGovernanceTaskProcessingResult]] = Field(default=None,alias="taskProcessingResults",)

from .identity_governance_lifecycle_workflow_processing_status import IdentityGovernanceLifecycleWorkflowProcessingStatus
from .identity_governance_task import IdentityGovernanceTask
from .identity_governance_task_definition import IdentityGovernanceTaskDefinition
from .identity_governance_task_processing_result import IdentityGovernanceTaskProcessingResult


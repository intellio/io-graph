from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class IdentityGovernanceRun(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	completedDateTime: Optional[datetime] = Field(alias="completedDateTime",default=None,)
	failedTasksCount: Optional[int] = Field(alias="failedTasksCount",default=None,)
	failedUsersCount: Optional[int] = Field(alias="failedUsersCount",default=None,)
	lastUpdatedDateTime: Optional[datetime] = Field(alias="lastUpdatedDateTime",default=None,)
	processingStatus: Optional[str | IdentityGovernanceLifecycleWorkflowProcessingStatus] = Field(alias="processingStatus",default=None,)
	scheduledDateTime: Optional[datetime] = Field(alias="scheduledDateTime",default=None,)
	startedDateTime: Optional[datetime] = Field(alias="startedDateTime",default=None,)
	successfulUsersCount: Optional[int] = Field(alias="successfulUsersCount",default=None,)
	totalTasksCount: Optional[int] = Field(alias="totalTasksCount",default=None,)
	totalUnprocessedTasksCount: Optional[int] = Field(alias="totalUnprocessedTasksCount",default=None,)
	totalUsersCount: Optional[int] = Field(alias="totalUsersCount",default=None,)
	workflowExecutionType: Optional[str | IdentityGovernanceWorkflowExecutionType] = Field(alias="workflowExecutionType",default=None,)
	taskProcessingResults: Optional[list[IdentityGovernanceTaskProcessingResult]] = Field(alias="taskProcessingResults",default=None,)
	userProcessingResults: Optional[list[IdentityGovernanceUserProcessingResult]] = Field(alias="userProcessingResults",default=None,)

from .identity_governance_lifecycle_workflow_processing_status import IdentityGovernanceLifecycleWorkflowProcessingStatus
from .identity_governance_workflow_execution_type import IdentityGovernanceWorkflowExecutionType
from .identity_governance_task_processing_result import IdentityGovernanceTaskProcessingResult
from .identity_governance_user_processing_result import IdentityGovernanceUserProcessingResult


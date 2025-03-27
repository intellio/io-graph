from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class IdentityGovernanceUserProcessingResult(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	completedDateTime: Optional[datetime] = Field(alias="completedDateTime", default=None,)
	failedTasksCount: Optional[int] = Field(alias="failedTasksCount", default=None,)
	processingStatus: Optional[IdentityGovernanceLifecycleWorkflowProcessingStatus | str] = Field(alias="processingStatus", default=None,)
	scheduledDateTime: Optional[datetime] = Field(alias="scheduledDateTime", default=None,)
	startedDateTime: Optional[datetime] = Field(alias="startedDateTime", default=None,)
	totalTasksCount: Optional[int] = Field(alias="totalTasksCount", default=None,)
	totalUnprocessedTasksCount: Optional[int] = Field(alias="totalUnprocessedTasksCount", default=None,)
	workflowExecutionType: Optional[IdentityGovernanceWorkflowExecutionType | str] = Field(alias="workflowExecutionType", default=None,)
	workflowVersion: Optional[int] = Field(alias="workflowVersion", default=None,)
	subject: Optional[User] = Field(alias="subject", default=None,)
	taskProcessingResults: Optional[list[IdentityGovernanceTaskProcessingResult]] = Field(alias="taskProcessingResults", default=None,)

from .identity_governance_lifecycle_workflow_processing_status import IdentityGovernanceLifecycleWorkflowProcessingStatus
from .identity_governance_workflow_execution_type import IdentityGovernanceWorkflowExecutionType
from .user import User
from .identity_governance_task_processing_result import IdentityGovernanceTaskProcessingResult


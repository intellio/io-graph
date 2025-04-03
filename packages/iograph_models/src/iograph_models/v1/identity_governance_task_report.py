from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class IdentityGovernanceTaskReport(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.identityGovernance.taskReport"] = Field(alias="@odata.type", default="#microsoft.graph.identityGovernance.taskReport")
	completedDateTime: Optional[datetime] = Field(alias="completedDateTime", default=None,)
	failedUsersCount: Optional[int] = Field(alias="failedUsersCount", default=None,)
	lastUpdatedDateTime: Optional[datetime] = Field(alias="lastUpdatedDateTime", default=None,)
	processingStatus: Optional[IdentityGovernanceLifecycleWorkflowProcessingStatus | str] = Field(alias="processingStatus", default=None,)
	runId: Optional[str] = Field(alias="runId", default=None,)
	startedDateTime: Optional[datetime] = Field(alias="startedDateTime", default=None,)
	successfulUsersCount: Optional[int] = Field(alias="successfulUsersCount", default=None,)
	totalUsersCount: Optional[int] = Field(alias="totalUsersCount", default=None,)
	unprocessedUsersCount: Optional[int] = Field(alias="unprocessedUsersCount", default=None,)
	task: Optional[IdentityGovernanceTask] = Field(alias="task", default=None,)
	taskDefinition: Optional[IdentityGovernanceTaskDefinition] = Field(alias="taskDefinition", default=None,)
	taskProcessingResults: Optional[list[IdentityGovernanceTaskProcessingResult]] = Field(alias="taskProcessingResults", default=None,)

from .identity_governance_lifecycle_workflow_processing_status import IdentityGovernanceLifecycleWorkflowProcessingStatus
from .identity_governance_task import IdentityGovernanceTask
from .identity_governance_task_definition import IdentityGovernanceTaskDefinition
from .identity_governance_task_processing_result import IdentityGovernanceTaskProcessingResult

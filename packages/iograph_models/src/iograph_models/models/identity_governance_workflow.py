from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class IdentityGovernanceWorkflow(BaseModel):
	category: Optional[IdentityGovernanceLifecycleWorkflowCategory] = Field(default=None,alias="category",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	executionConditions: Optional[IdentityGovernanceWorkflowExecutionConditions] = Field(default=None,alias="executionConditions",)
	isEnabled: Optional[bool] = Field(default=None,alias="isEnabled",)
	isSchedulingEnabled: Optional[bool] = Field(default=None,alias="isSchedulingEnabled",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	createdBy: Optional[User] = Field(default=None,alias="createdBy",)
	lastModifiedBy: Optional[User] = Field(default=None,alias="lastModifiedBy",)
	tasks: list[IdentityGovernanceTask] = Field(alias="tasks",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	deletedDateTime: Optional[datetime] = Field(default=None,alias="deletedDateTime",)
	id: Optional[str] = Field(default=None,alias="id",)
	nextScheduleRunDateTime: Optional[datetime] = Field(default=None,alias="nextScheduleRunDateTime",)
	version: Optional[int] = Field(default=None,alias="version",)
	executionScope: list[IdentityGovernanceUserProcessingResult] = Field(alias="executionScope",)
	runs: list[IdentityGovernanceRun] = Field(alias="runs",)
	taskReports: list[IdentityGovernanceTaskReport] = Field(alias="taskReports",)
	userProcessingResults: list[IdentityGovernanceUserProcessingResult] = Field(alias="userProcessingResults",)
	versions: list[IdentityGovernanceWorkflowVersion] = Field(alias="versions",)

from .identity_governance_lifecycle_workflow_category import IdentityGovernanceLifecycleWorkflowCategory
from .identity_governance_workflow_execution_conditions import IdentityGovernanceWorkflowExecutionConditions
from .user import User
from .user import User
from .identity_governance_task import IdentityGovernanceTask
from .identity_governance_user_processing_result import IdentityGovernanceUserProcessingResult
from .identity_governance_run import IdentityGovernanceRun
from .identity_governance_task_report import IdentityGovernanceTaskReport
from .identity_governance_user_processing_result import IdentityGovernanceUserProcessingResult
from .identity_governance_workflow_version import IdentityGovernanceWorkflowVersion


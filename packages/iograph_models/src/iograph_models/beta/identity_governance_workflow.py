from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class IdentityGovernanceWorkflow(BaseModel):
	category: Optional[IdentityGovernanceLifecycleWorkflowCategory | str] = Field(alias="category", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	executionConditions: Optional[Union[IdentityGovernanceOnDemandExecutionOnly, IdentityGovernanceTriggerAndScopeBasedConditions]] = Field(alias="executionConditions", default=None,discriminator="odata_type", )
	isEnabled: Optional[bool] = Field(alias="isEnabled", default=None,)
	isSchedulingEnabled: Optional[bool] = Field(alias="isSchedulingEnabled", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	createdBy: Optional[User] = Field(alias="createdBy", default=None,)
	lastModifiedBy: Optional[User] = Field(alias="lastModifiedBy", default=None,)
	tasks: Optional[list[IdentityGovernanceTask]] = Field(alias="tasks", default=None,)
	odata_type: Literal["#microsoft.graph.identityGovernance.workflow"] = Field(alias="@odata.type", default="#microsoft.graph.identityGovernance.workflow")
	deletedDateTime: Optional[datetime] = Field(alias="deletedDateTime", default=None,)
	id: Optional[str] = Field(alias="id", default=None,)
	nextScheduleRunDateTime: Optional[datetime] = Field(alias="nextScheduleRunDateTime", default=None,)
	version: Optional[int] = Field(alias="version", default=None,)
	executionScope: Optional[list[IdentityGovernanceUserProcessingResult]] = Field(alias="executionScope", default=None,)
	runs: Optional[list[IdentityGovernanceRun]] = Field(alias="runs", default=None,)
	taskReports: Optional[list[IdentityGovernanceTaskReport]] = Field(alias="taskReports", default=None,)
	userProcessingResults: Optional[list[IdentityGovernanceUserProcessingResult]] = Field(alias="userProcessingResults", default=None,)
	versions: Optional[list[IdentityGovernanceWorkflowVersion]] = Field(alias="versions", default=None,)

from .identity_governance_lifecycle_workflow_category import IdentityGovernanceLifecycleWorkflowCategory
from .identity_governance_on_demand_execution_only import IdentityGovernanceOnDemandExecutionOnly
from .identity_governance_trigger_and_scope_based_conditions import IdentityGovernanceTriggerAndScopeBasedConditions
from .user import User
from .user import User
from .identity_governance_task import IdentityGovernanceTask
from .identity_governance_user_processing_result import IdentityGovernanceUserProcessingResult
from .identity_governance_run import IdentityGovernanceRun
from .identity_governance_task_report import IdentityGovernanceTaskReport
from .identity_governance_user_processing_result import IdentityGovernanceUserProcessingResult
from .identity_governance_workflow_version import IdentityGovernanceWorkflowVersion


from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class IdentityGovernanceWorkflowVersion(BaseModel):
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
	odata_type: Literal["#microsoft.graph.identityGovernance.workflowVersion"] = Field(alias="@odata.type", default="#microsoft.graph.identityGovernance.workflowVersion")
	versionNumber: Optional[int] = Field(alias="versionNumber", default=None,)

from .identity_governance_lifecycle_workflow_category import IdentityGovernanceLifecycleWorkflowCategory
from .identity_governance_on_demand_execution_only import IdentityGovernanceOnDemandExecutionOnly
from .identity_governance_trigger_and_scope_based_conditions import IdentityGovernanceTriggerAndScopeBasedConditions
from .user import User
from .identity_governance_task import IdentityGovernanceTask

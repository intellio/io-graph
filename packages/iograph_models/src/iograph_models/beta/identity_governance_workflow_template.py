from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import BaseModel, Field


class IdentityGovernanceWorkflowTemplate(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.identityGovernance.workflowTemplate"] = Field(alias="@odata.type",)
	category: Optional[IdentityGovernanceLifecycleWorkflowCategory | str] = Field(alias="category", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	executionConditions: Optional[Union[IdentityGovernanceOnDemandExecutionOnly, IdentityGovernanceTriggerAndScopeBasedConditions]] = Field(alias="executionConditions", default=None,discriminator="odata_type", )
	tasks: Optional[list[IdentityGovernanceTask]] = Field(alias="tasks", default=None,)

from .identity_governance_lifecycle_workflow_category import IdentityGovernanceLifecycleWorkflowCategory
from .identity_governance_on_demand_execution_only import IdentityGovernanceOnDemandExecutionOnly
from .identity_governance_trigger_and_scope_based_conditions import IdentityGovernanceTriggerAndScopeBasedConditions
from .identity_governance_task import IdentityGovernanceTask

from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class IdentityGovernanceLifecycleWorkflowsContainer(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.identityGovernance.lifecycleWorkflowsContainer"] = Field(alias="@odata.type", default="#microsoft.graph.identityGovernance.lifecycleWorkflowsContainer")
	customTaskExtensions: Optional[list[IdentityGovernanceCustomTaskExtension]] = Field(alias="customTaskExtensions", default=None,)
	deletedItems: Optional[DeletedItemContainer] = Field(alias="deletedItems", default=None,)
	insights: Optional[IdentityGovernanceInsights] = Field(alias="insights", default=None,)
	settings: Optional[IdentityGovernanceLifecycleManagementSettings] = Field(alias="settings", default=None,)
	taskDefinitions: Optional[list[IdentityGovernanceTaskDefinition]] = Field(alias="taskDefinitions", default=None,)
	workflows: Optional[list[IdentityGovernanceWorkflow]] = Field(alias="workflows", default=None,)
	workflowTemplates: Optional[list[IdentityGovernanceWorkflowTemplate]] = Field(alias="workflowTemplates", default=None,)

from .identity_governance_custom_task_extension import IdentityGovernanceCustomTaskExtension
from .deleted_item_container import DeletedItemContainer
from .identity_governance_insights import IdentityGovernanceInsights
from .identity_governance_lifecycle_management_settings import IdentityGovernanceLifecycleManagementSettings
from .identity_governance_task_definition import IdentityGovernanceTaskDefinition
from .identity_governance_workflow import IdentityGovernanceWorkflow
from .identity_governance_workflow_template import IdentityGovernanceWorkflowTemplate

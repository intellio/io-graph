from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IdentityGovernanceLifecycleWorkflowsContainer(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	customTaskExtensions: list[IdentityGovernanceCustomTaskExtension] = Field(alias="customTaskExtensions",)
	deletedItems: Optional[DeletedItemContainer] = Field(default=None,alias="deletedItems",)
	insights: Optional[IdentityGovernanceInsights] = Field(default=None,alias="insights",)
	settings: Optional[IdentityGovernanceLifecycleManagementSettings] = Field(default=None,alias="settings",)
	taskDefinitions: list[IdentityGovernanceTaskDefinition] = Field(alias="taskDefinitions",)
	workflows: list[IdentityGovernanceWorkflow] = Field(alias="workflows",)
	workflowTemplates: list[IdentityGovernanceWorkflowTemplate] = Field(alias="workflowTemplates",)

from .identity_governance_custom_task_extension import IdentityGovernanceCustomTaskExtension
from .deleted_item_container import DeletedItemContainer
from .identity_governance_insights import IdentityGovernanceInsights
from .identity_governance_lifecycle_management_settings import IdentityGovernanceLifecycleManagementSettings
from .identity_governance_task_definition import IdentityGovernanceTaskDefinition
from .identity_governance_workflow import IdentityGovernanceWorkflow
from .identity_governance_workflow_template import IdentityGovernanceWorkflowTemplate


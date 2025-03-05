from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IdentityGovernanceWorkflowTemplate(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	category: Optional[IdentityGovernanceLifecycleWorkflowCategory] = Field(default=None,alias="category",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	executionConditions: SerializeAsAny[Optional[IdentityGovernanceWorkflowExecutionConditions]] = Field(default=None,alias="executionConditions",)
	tasks: Optional[list[IdentityGovernanceTask]] = Field(default=None,alias="tasks",)

from .identity_governance_lifecycle_workflow_category import IdentityGovernanceLifecycleWorkflowCategory
from .identity_governance_workflow_execution_conditions import IdentityGovernanceWorkflowExecutionConditions
from .identity_governance_task import IdentityGovernanceTask


from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class IdentityGovernanceWorkflowVersion(BaseModel):
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
	tasks: Optional[list[IdentityGovernanceTask]] = Field(default=None,alias="tasks",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	versionNumber: Optional[int] = Field(default=None,alias="versionNumber",)

from .identity_governance_lifecycle_workflow_category import IdentityGovernanceLifecycleWorkflowCategory
from .identity_governance_workflow_execution_conditions import IdentityGovernanceWorkflowExecutionConditions
from .user import User
from .user import User
from .identity_governance_task import IdentityGovernanceTask


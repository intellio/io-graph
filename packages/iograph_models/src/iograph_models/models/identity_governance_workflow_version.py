from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class IdentityGovernanceWorkflowVersion(BaseModel):
	category: Optional[IdentityGovernanceLifecycleWorkflowCategory | str] = Field(alias="category",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	executionConditions: SerializeAsAny[Optional[IdentityGovernanceWorkflowExecutionConditions]] = Field(alias="executionConditions",default=None,)
	isEnabled: Optional[bool] = Field(alias="isEnabled",default=None,)
	isSchedulingEnabled: Optional[bool] = Field(alias="isSchedulingEnabled",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	createdBy: Optional[User] = Field(alias="createdBy",default=None,)
	lastModifiedBy: Optional[User] = Field(alias="lastModifiedBy",default=None,)
	tasks: Optional[list[IdentityGovernanceTask]] = Field(alias="tasks",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	versionNumber: Optional[int] = Field(alias="versionNumber",default=None,)

from .identity_governance_lifecycle_workflow_category import IdentityGovernanceLifecycleWorkflowCategory
from .identity_governance_workflow_execution_conditions import IdentityGovernanceWorkflowExecutionConditions
from .user import User
from .user import User
from .identity_governance_task import IdentityGovernanceTask


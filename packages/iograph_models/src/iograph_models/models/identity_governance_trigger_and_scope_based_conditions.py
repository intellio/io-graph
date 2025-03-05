from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IdentityGovernanceTriggerAndScopeBasedConditions(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	scope: SerializeAsAny[Optional[SubjectSet]] = Field(default=None,alias="scope",)
	trigger: SerializeAsAny[Optional[IdentityGovernanceWorkflowExecutionTrigger]] = Field(default=None,alias="trigger",)

from .subject_set import SubjectSet
from .identity_governance_workflow_execution_trigger import IdentityGovernanceWorkflowExecutionTrigger


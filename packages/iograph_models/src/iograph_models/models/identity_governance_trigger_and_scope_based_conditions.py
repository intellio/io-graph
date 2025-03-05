from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IdentityGovernanceTriggerAndScopeBasedConditions(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	scope: SerializeAsAny[Optional[SubjectSet]] = Field(alias="scope",default=None,)
	trigger: SerializeAsAny[Optional[IdentityGovernanceWorkflowExecutionTrigger]] = Field(alias="trigger",default=None,)

from .subject_set import SubjectSet
from .identity_governance_workflow_execution_trigger import IdentityGovernanceWorkflowExecutionTrigger


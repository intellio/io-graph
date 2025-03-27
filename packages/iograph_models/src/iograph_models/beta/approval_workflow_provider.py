from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ApprovalWorkflowProvider(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	businessFlows: Optional[list[BusinessFlow]] = Field(alias="businessFlows", default=None,)
	businessFlowsWithRequestsAwaitingMyDecision: Optional[list[BusinessFlow]] = Field(alias="businessFlowsWithRequestsAwaitingMyDecision", default=None,)
	policyTemplates: Optional[list[GovernancePolicyTemplate]] = Field(alias="policyTemplates", default=None,)

from .business_flow import BusinessFlow
from .business_flow import BusinessFlow
from .governance_policy_template import GovernancePolicyTemplate


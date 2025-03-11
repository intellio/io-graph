from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TeamsAdministrationEffectivePolicyAssignment(BaseModel):
	policyAssignment: Optional[TeamsAdministrationPolicyAssignment] = Field(alias="policyAssignment",default=None,)
	policyType: Optional[str] = Field(alias="policyType",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .teams_administration_policy_assignment import TeamsAdministrationPolicyAssignment


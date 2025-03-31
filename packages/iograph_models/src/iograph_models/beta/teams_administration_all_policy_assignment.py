from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TeamsAdministrationAllPolicyAssignment(BaseModel):
	policyAssignments: Optional[list[TeamsAdministrationPolicyAssignment]] = Field(alias="policyAssignments", default=None,)
	policyType: Optional[str] = Field(alias="policyType", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .teams_administration_policy_assignment import TeamsAdministrationPolicyAssignment

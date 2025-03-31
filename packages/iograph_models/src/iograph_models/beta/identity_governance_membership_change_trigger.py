from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class IdentityGovernanceMembershipChangeTrigger(BaseModel):
	odata_type: Literal["#microsoft.graph.identityGovernance.membershipChangeTrigger"] = Field(alias="@odata.type", default="#microsoft.graph.identityGovernance.membershipChangeTrigger")
	changeType: Optional[IdentityGovernanceMembershipChangeType | str] = Field(alias="changeType", default=None,)

from .identity_governance_membership_change_type import IdentityGovernanceMembershipChangeType

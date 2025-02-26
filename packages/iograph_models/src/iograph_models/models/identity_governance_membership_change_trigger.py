from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IdentityGovernanceMembershipChangeTrigger(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	changeType: Optional[IdentityGovernanceMembershipChangeType] = Field(default=None,alias="changeType",)

from .identity_governance_membership_change_type import IdentityGovernanceMembershipChangeType


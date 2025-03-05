from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IdentityGovernanceMembershipChangeTrigger(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	changeType: Optional[str | IdentityGovernanceMembershipChangeType] = Field(alias="changeType",default=None,)

from .identity_governance_membership_change_type import IdentityGovernanceMembershipChangeType


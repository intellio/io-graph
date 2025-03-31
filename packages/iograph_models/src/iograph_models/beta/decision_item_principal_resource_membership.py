from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DecisionItemPrincipalResourceMembership(BaseModel):
	membershipType: Optional[DecisionItemPrincipalResourceMembershipType | str] = Field(alias="membershipType", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .decision_item_principal_resource_membership_type import DecisionItemPrincipalResourceMembershipType

from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ChannelSummary(BaseModel):
	guestsCount: Optional[int] = Field(default=None,alias="guestsCount",)
	hasMembersFromOtherTenants: Optional[bool] = Field(default=None,alias="hasMembersFromOtherTenants",)
	membersCount: Optional[int] = Field(default=None,alias="membersCount",)
	ownersCount: Optional[int] = Field(default=None,alias="ownersCount",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)



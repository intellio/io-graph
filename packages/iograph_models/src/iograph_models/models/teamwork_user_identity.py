from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TeamworkUserIdentity(BaseModel):
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	userIdentityType: Optional[TeamworkUserIdentityType] = Field(default=None,alias="userIdentityType",)

from .teamwork_user_identity_type import TeamworkUserIdentityType


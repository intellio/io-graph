from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class TeamworkUserIdentity(BaseModel):
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.teamworkUserIdentity"] = Field(alias="@odata.type", default="#microsoft.graph.teamworkUserIdentity")
	userIdentityType: Optional[TeamworkUserIdentityType | str] = Field(alias="userIdentityType", default=None,)

from .teamwork_user_identity_type import TeamworkUserIdentityType

from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SharedWithChannelTeamInfo(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	tenantId: Optional[str] = Field(default=None,alias="tenantId",)
	team: Optional[Team] = Field(default=None,alias="team",)
	isHostTeam: Optional[bool] = Field(default=None,alias="isHostTeam",)
	allowedMembers: list[ConversationMember] = Field(alias="allowedMembers",)

from .team import Team
from .conversation_member import ConversationMember


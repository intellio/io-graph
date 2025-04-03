from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class TeamworkTag(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.teamworkTag"] = Field(alias="@odata.type", default="#microsoft.graph.teamworkTag")
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	memberCount: Optional[int] = Field(alias="memberCount", default=None,)
	tagType: Optional[TeamworkTagType | str] = Field(alias="tagType", default=None,)
	teamId: Optional[str] = Field(alias="teamId", default=None,)
	members: Optional[list[TeamworkTagMember]] = Field(alias="members", default=None,)

from .teamwork_tag_type import TeamworkTagType
from .teamwork_tag_member import TeamworkTagMember

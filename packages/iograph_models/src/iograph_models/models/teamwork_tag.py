from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TeamworkTag(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	memberCount: Optional[int] = Field(default=None,alias="memberCount",)
	tagType: Optional[TeamworkTagType] = Field(default=None,alias="tagType",)
	teamId: Optional[str] = Field(default=None,alias="teamId",)
	members: Optional[list[TeamworkTagMember]] = Field(default=None,alias="members",)

from .teamwork_tag_type import TeamworkTagType
from .teamwork_tag_member import TeamworkTagMember


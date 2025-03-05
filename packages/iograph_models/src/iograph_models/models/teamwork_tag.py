from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TeamworkTag(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	memberCount: Optional[int] = Field(alias="memberCount",default=None,)
	tagType: Optional[str | TeamworkTagType] = Field(alias="tagType",default=None,)
	teamId: Optional[str] = Field(alias="teamId",default=None,)
	members: Optional[list[TeamworkTagMember]] = Field(alias="members",default=None,)

from .teamwork_tag_type import TeamworkTagType
from .teamwork_tag_member import TeamworkTagMember


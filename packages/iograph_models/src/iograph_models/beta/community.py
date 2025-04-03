from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class Community(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.community"] = Field(alias="@odata.type", default="#microsoft.graph.community")
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	groupId: Optional[str] = Field(alias="groupId", default=None,)
	privacy: Optional[CommunityPrivacy | str] = Field(alias="privacy", default=None,)
	group: Optional[Group] = Field(alias="group", default=None,)
	owners: Optional[list[User]] = Field(alias="owners", default=None,)

from .community_privacy import CommunityPrivacy
from .group import Group
from .user import User

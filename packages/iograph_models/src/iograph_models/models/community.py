from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Community(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	groupId: Optional[str] = Field(default=None,alias="groupId",)
	privacy: Optional[CommunityPrivacy] = Field(default=None,alias="privacy",)
	group: Optional[Group] = Field(default=None,alias="group",)
	owners: Optional[list[User]] = Field(default=None,alias="owners",)

from .community_privacy import CommunityPrivacy
from .group import Group
from .user import User


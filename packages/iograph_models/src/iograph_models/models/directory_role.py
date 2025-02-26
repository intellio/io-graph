from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class DirectoryRole(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	deletedDateTime: Optional[datetime] = Field(default=None,alias="deletedDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	roleTemplateId: Optional[str] = Field(default=None,alias="roleTemplateId",)
	members: list[DirectoryObject] = Field(alias="members",)
	scopedMembers: list[ScopedRoleMembership] = Field(alias="scopedMembers",)

from .directory_object import DirectoryObject
from .scoped_role_membership import ScopedRoleMembership


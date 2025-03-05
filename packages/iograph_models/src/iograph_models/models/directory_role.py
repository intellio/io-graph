from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class DirectoryRole(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	deletedDateTime: Optional[datetime] = Field(alias="deletedDateTime",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	roleTemplateId: Optional[str] = Field(alias="roleTemplateId",default=None,)
	members: SerializeAsAny[Optional[list[DirectoryObject]]] = Field(alias="members",default=None,)
	scopedMembers: Optional[list[ScopedRoleMembership]] = Field(alias="scopedMembers",default=None,)

from .directory_object import DirectoryObject
from .scoped_role_membership import ScopedRoleMembership


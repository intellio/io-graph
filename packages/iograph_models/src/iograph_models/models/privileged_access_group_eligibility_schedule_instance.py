from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class PrivilegedAccessGroupEligibilityScheduleInstance(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	endDateTime: Optional[datetime] = Field(default=None,alias="endDateTime",)
	startDateTime: Optional[datetime] = Field(default=None,alias="startDateTime",)
	accessId: Optional[PrivilegedAccessGroupRelationships] = Field(default=None,alias="accessId",)
	eligibilityScheduleId: Optional[str] = Field(default=None,alias="eligibilityScheduleId",)
	groupId: Optional[str] = Field(default=None,alias="groupId",)
	memberType: Optional[PrivilegedAccessGroupMemberType] = Field(default=None,alias="memberType",)
	principalId: Optional[str] = Field(default=None,alias="principalId",)
	group: Optional[Group] = Field(default=None,alias="group",)
	principal: SerializeAsAny[Optional[DirectoryObject]] = Field(default=None,alias="principal",)

from .privileged_access_group_relationships import PrivilegedAccessGroupRelationships
from .privileged_access_group_member_type import PrivilegedAccessGroupMemberType
from .group import Group
from .directory_object import DirectoryObject


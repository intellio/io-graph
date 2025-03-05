from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class PrivilegedAccessGroupEligibilityScheduleInstance(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	endDateTime: Optional[datetime] = Field(alias="endDateTime",default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime",default=None,)
	accessId: Optional[str | PrivilegedAccessGroupRelationships] = Field(alias="accessId",default=None,)
	eligibilityScheduleId: Optional[str] = Field(alias="eligibilityScheduleId",default=None,)
	groupId: Optional[str] = Field(alias="groupId",default=None,)
	memberType: Optional[str | PrivilegedAccessGroupMemberType] = Field(alias="memberType",default=None,)
	principalId: Optional[str] = Field(alias="principalId",default=None,)
	group: Optional[Group] = Field(alias="group",default=None,)
	principal: SerializeAsAny[Optional[DirectoryObject]] = Field(alias="principal",default=None,)

from .privileged_access_group_relationships import PrivilegedAccessGroupRelationships
from .privileged_access_group_member_type import PrivilegedAccessGroupMemberType
from .group import Group
from .directory_object import DirectoryObject


from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class PrivilegedAccessGroupEligibilitySchedule(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	createdUsing: Optional[str] = Field(default=None,alias="createdUsing",)
	modifiedDateTime: Optional[datetime] = Field(default=None,alias="modifiedDateTime",)
	scheduleInfo: Optional[RequestSchedule] = Field(default=None,alias="scheduleInfo",)
	status: Optional[str] = Field(default=None,alias="status",)
	accessId: Optional[PrivilegedAccessGroupRelationships] = Field(default=None,alias="accessId",)
	groupId: Optional[str] = Field(default=None,alias="groupId",)
	memberType: Optional[PrivilegedAccessGroupMemberType] = Field(default=None,alias="memberType",)
	principalId: Optional[str] = Field(default=None,alias="principalId",)
	group: Optional[Group] = Field(default=None,alias="group",)
	principal: Optional[DirectoryObject] = Field(default=None,alias="principal",)

from .request_schedule import RequestSchedule
from .privileged_access_group_relationships import PrivilegedAccessGroupRelationships
from .privileged_access_group_member_type import PrivilegedAccessGroupMemberType
from .group import Group
from .directory_object import DirectoryObject


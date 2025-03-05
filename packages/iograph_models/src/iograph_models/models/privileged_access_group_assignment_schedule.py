from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class PrivilegedAccessGroupAssignmentSchedule(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	createdUsing: Optional[str] = Field(alias="createdUsing",default=None,)
	modifiedDateTime: Optional[datetime] = Field(alias="modifiedDateTime",default=None,)
	scheduleInfo: Optional[RequestSchedule] = Field(alias="scheduleInfo",default=None,)
	status: Optional[str] = Field(alias="status",default=None,)
	accessId: Optional[PrivilegedAccessGroupRelationships | str] = Field(alias="accessId",default=None,)
	assignmentType: Optional[PrivilegedAccessGroupAssignmentType | str] = Field(alias="assignmentType",default=None,)
	groupId: Optional[str] = Field(alias="groupId",default=None,)
	memberType: Optional[PrivilegedAccessGroupMemberType | str] = Field(alias="memberType",default=None,)
	principalId: Optional[str] = Field(alias="principalId",default=None,)
	activatedUsing: Optional[PrivilegedAccessGroupEligibilitySchedule] = Field(alias="activatedUsing",default=None,)
	group: Optional[Group] = Field(alias="group",default=None,)
	principal: SerializeAsAny[Optional[DirectoryObject]] = Field(alias="principal",default=None,)

from .request_schedule import RequestSchedule
from .privileged_access_group_relationships import PrivilegedAccessGroupRelationships
from .privileged_access_group_assignment_type import PrivilegedAccessGroupAssignmentType
from .privileged_access_group_member_type import PrivilegedAccessGroupMemberType
from .privileged_access_group_eligibility_schedule import PrivilegedAccessGroupEligibilitySchedule
from .group import Group
from .directory_object import DirectoryObject


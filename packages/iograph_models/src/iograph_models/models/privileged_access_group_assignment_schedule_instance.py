from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class PrivilegedAccessGroupAssignmentScheduleInstance(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	endDateTime: Optional[datetime] = Field(alias="endDateTime",default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime",default=None,)
	accessId: Optional[str | PrivilegedAccessGroupRelationships] = Field(alias="accessId",default=None,)
	assignmentScheduleId: Optional[str] = Field(alias="assignmentScheduleId",default=None,)
	assignmentType: Optional[str | PrivilegedAccessGroupAssignmentType] = Field(alias="assignmentType",default=None,)
	groupId: Optional[str] = Field(alias="groupId",default=None,)
	memberType: Optional[str | PrivilegedAccessGroupMemberType] = Field(alias="memberType",default=None,)
	principalId: Optional[str] = Field(alias="principalId",default=None,)
	activatedUsing: Optional[PrivilegedAccessGroupEligibilityScheduleInstance] = Field(alias="activatedUsing",default=None,)
	group: Optional[Group] = Field(alias="group",default=None,)
	principal: SerializeAsAny[Optional[DirectoryObject]] = Field(alias="principal",default=None,)

from .privileged_access_group_relationships import PrivilegedAccessGroupRelationships
from .privileged_access_group_assignment_type import PrivilegedAccessGroupAssignmentType
from .privileged_access_group_member_type import PrivilegedAccessGroupMemberType
from .privileged_access_group_eligibility_schedule_instance import PrivilegedAccessGroupEligibilityScheduleInstance
from .group import Group
from .directory_object import DirectoryObject


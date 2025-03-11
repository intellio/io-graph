from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class PrivilegedAccessGroupAssignmentScheduleRequest(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	approvalId: Optional[str] = Field(alias="approvalId",default=None,)
	completedDateTime: Optional[datetime] = Field(alias="completedDateTime",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	customData: Optional[str] = Field(alias="customData",default=None,)
	status: Optional[str] = Field(alias="status",default=None,)
	action: Optional[ScheduleRequestActions | str] = Field(alias="action",default=None,)
	isValidationOnly: Optional[bool] = Field(alias="isValidationOnly",default=None,)
	justification: Optional[str] = Field(alias="justification",default=None,)
	scheduleInfo: Optional[RequestSchedule] = Field(alias="scheduleInfo",default=None,)
	ticketInfo: Optional[TicketInfo] = Field(alias="ticketInfo",default=None,)
	accessId: Optional[PrivilegedAccessGroupRelationships | str] = Field(alias="accessId",default=None,)
	groupId: Optional[str] = Field(alias="groupId",default=None,)
	principalId: Optional[str] = Field(alias="principalId",default=None,)
	targetScheduleId: Optional[str] = Field(alias="targetScheduleId",default=None,)
	activatedUsing: Optional[PrivilegedAccessGroupEligibilitySchedule] = Field(alias="activatedUsing",default=None,)
	group: Optional[Group] = Field(alias="group",default=None,)
	principal: SerializeAsAny[Optional[DirectoryObject]] = Field(alias="principal",default=None,)
	targetSchedule: Optional[PrivilegedAccessGroupEligibilitySchedule] = Field(alias="targetSchedule",default=None,)

from .identity_set import IdentitySet
from .schedule_request_actions import ScheduleRequestActions
from .request_schedule import RequestSchedule
from .ticket_info import TicketInfo
from .privileged_access_group_relationships import PrivilegedAccessGroupRelationships
from .privileged_access_group_eligibility_schedule import PrivilegedAccessGroupEligibilitySchedule
from .group import Group
from .directory_object import DirectoryObject
from .privileged_access_group_eligibility_schedule import PrivilegedAccessGroupEligibilitySchedule


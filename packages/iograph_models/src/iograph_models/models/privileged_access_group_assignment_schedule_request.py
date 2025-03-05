from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class PrivilegedAccessGroupAssignmentScheduleRequest(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	approvalId: Optional[str] = Field(default=None,alias="approvalId",)
	completedDateTime: Optional[datetime] = Field(default=None,alias="completedDateTime",)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="createdBy",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	customData: Optional[str] = Field(default=None,alias="customData",)
	status: Optional[str] = Field(default=None,alias="status",)
	action: Optional[ScheduleRequestActions] = Field(default=None,alias="action",)
	isValidationOnly: Optional[bool] = Field(default=None,alias="isValidationOnly",)
	justification: Optional[str] = Field(default=None,alias="justification",)
	scheduleInfo: Optional[RequestSchedule] = Field(default=None,alias="scheduleInfo",)
	ticketInfo: Optional[TicketInfo] = Field(default=None,alias="ticketInfo",)
	accessId: Optional[PrivilegedAccessGroupRelationships] = Field(default=None,alias="accessId",)
	groupId: Optional[str] = Field(default=None,alias="groupId",)
	principalId: Optional[str] = Field(default=None,alias="principalId",)
	targetScheduleId: Optional[str] = Field(default=None,alias="targetScheduleId",)
	activatedUsing: Optional[PrivilegedAccessGroupEligibilitySchedule] = Field(default=None,alias="activatedUsing",)
	group: Optional[Group] = Field(default=None,alias="group",)
	principal: SerializeAsAny[Optional[DirectoryObject]] = Field(default=None,alias="principal",)
	targetSchedule: Optional[PrivilegedAccessGroupEligibilitySchedule] = Field(default=None,alias="targetSchedule",)

from .identity_set import IdentitySet
from .schedule_request_actions import ScheduleRequestActions
from .request_schedule import RequestSchedule
from .ticket_info import TicketInfo
from .privileged_access_group_relationships import PrivilegedAccessGroupRelationships
from .privileged_access_group_eligibility_schedule import PrivilegedAccessGroupEligibilitySchedule
from .group import Group
from .directory_object import DirectoryObject
from .privileged_access_group_eligibility_schedule import PrivilegedAccessGroupEligibilitySchedule


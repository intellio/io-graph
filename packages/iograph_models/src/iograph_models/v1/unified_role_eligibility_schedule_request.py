from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class UnifiedRoleEligibilityScheduleRequest(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	approvalId: Optional[str] = Field(alias="approvalId",default=None,)
	completedDateTime: Optional[datetime] = Field(alias="completedDateTime",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	customData: Optional[str] = Field(alias="customData",default=None,)
	status: Optional[str] = Field(alias="status",default=None,)
	action: Optional[UnifiedRoleScheduleRequestActions | str] = Field(alias="action",default=None,)
	appScopeId: Optional[str] = Field(alias="appScopeId",default=None,)
	directoryScopeId: Optional[str] = Field(alias="directoryScopeId",default=None,)
	isValidationOnly: Optional[bool] = Field(alias="isValidationOnly",default=None,)
	justification: Optional[str] = Field(alias="justification",default=None,)
	principalId: Optional[str] = Field(alias="principalId",default=None,)
	roleDefinitionId: Optional[str] = Field(alias="roleDefinitionId",default=None,)
	scheduleInfo: Optional[RequestSchedule] = Field(alias="scheduleInfo",default=None,)
	targetScheduleId: Optional[str] = Field(alias="targetScheduleId",default=None,)
	ticketInfo: Optional[TicketInfo] = Field(alias="ticketInfo",default=None,)
	appScope: Optional[AppScope] = Field(alias="appScope",default=None,)
	directoryScope: SerializeAsAny[Optional[DirectoryObject]] = Field(alias="directoryScope",default=None,)
	principal: SerializeAsAny[Optional[DirectoryObject]] = Field(alias="principal",default=None,)
	roleDefinition: Optional[UnifiedRoleDefinition] = Field(alias="roleDefinition",default=None,)
	targetSchedule: Optional[UnifiedRoleEligibilitySchedule] = Field(alias="targetSchedule",default=None,)

from .identity_set import IdentitySet
from .unified_role_schedule_request_actions import UnifiedRoleScheduleRequestActions
from .request_schedule import RequestSchedule
from .ticket_info import TicketInfo
from .app_scope import AppScope
from .directory_object import DirectoryObject
from .directory_object import DirectoryObject
from .unified_role_definition import UnifiedRoleDefinition
from .unified_role_eligibility_schedule import UnifiedRoleEligibilitySchedule


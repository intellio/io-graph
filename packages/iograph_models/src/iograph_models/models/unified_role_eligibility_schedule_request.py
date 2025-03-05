from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class UnifiedRoleEligibilityScheduleRequest(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	approvalId: Optional[str] = Field(default=None,alias="approvalId",)
	completedDateTime: Optional[datetime] = Field(default=None,alias="completedDateTime",)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="createdBy",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	customData: Optional[str] = Field(default=None,alias="customData",)
	status: Optional[str] = Field(default=None,alias="status",)
	action: Optional[UnifiedRoleScheduleRequestActions] = Field(default=None,alias="action",)
	appScopeId: Optional[str] = Field(default=None,alias="appScopeId",)
	directoryScopeId: Optional[str] = Field(default=None,alias="directoryScopeId",)
	isValidationOnly: Optional[bool] = Field(default=None,alias="isValidationOnly",)
	justification: Optional[str] = Field(default=None,alias="justification",)
	principalId: Optional[str] = Field(default=None,alias="principalId",)
	roleDefinitionId: Optional[str] = Field(default=None,alias="roleDefinitionId",)
	scheduleInfo: Optional[RequestSchedule] = Field(default=None,alias="scheduleInfo",)
	targetScheduleId: Optional[str] = Field(default=None,alias="targetScheduleId",)
	ticketInfo: Optional[TicketInfo] = Field(default=None,alias="ticketInfo",)
	appScope: Optional[AppScope] = Field(default=None,alias="appScope",)
	directoryScope: SerializeAsAny[Optional[DirectoryObject]] = Field(default=None,alias="directoryScope",)
	principal: SerializeAsAny[Optional[DirectoryObject]] = Field(default=None,alias="principal",)
	roleDefinition: Optional[UnifiedRoleDefinition] = Field(default=None,alias="roleDefinition",)
	targetSchedule: Optional[UnifiedRoleEligibilitySchedule] = Field(default=None,alias="targetSchedule",)

from .identity_set import IdentitySet
from .unified_role_schedule_request_actions import UnifiedRoleScheduleRequestActions
from .request_schedule import RequestSchedule
from .ticket_info import TicketInfo
from .app_scope import AppScope
from .directory_object import DirectoryObject
from .directory_object import DirectoryObject
from .unified_role_definition import UnifiedRoleDefinition
from .unified_role_eligibility_schedule import UnifiedRoleEligibilitySchedule


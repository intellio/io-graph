from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class UnifiedRoleAssignmentScheduleInstance(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	appScopeId: Optional[str] = Field(alias="appScopeId",default=None,)
	directoryScopeId: Optional[str] = Field(alias="directoryScopeId",default=None,)
	principalId: Optional[str] = Field(alias="principalId",default=None,)
	roleDefinitionId: Optional[str] = Field(alias="roleDefinitionId",default=None,)
	appScope: Optional[AppScope] = Field(alias="appScope",default=None,)
	directoryScope: SerializeAsAny[Optional[DirectoryObject]] = Field(alias="directoryScope",default=None,)
	principal: SerializeAsAny[Optional[DirectoryObject]] = Field(alias="principal",default=None,)
	roleDefinition: Optional[UnifiedRoleDefinition] = Field(alias="roleDefinition",default=None,)
	assignmentType: Optional[str] = Field(alias="assignmentType",default=None,)
	endDateTime: Optional[datetime] = Field(alias="endDateTime",default=None,)
	memberType: Optional[str] = Field(alias="memberType",default=None,)
	roleAssignmentOriginId: Optional[str] = Field(alias="roleAssignmentOriginId",default=None,)
	roleAssignmentScheduleId: Optional[str] = Field(alias="roleAssignmentScheduleId",default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime",default=None,)
	activatedUsing: Optional[UnifiedRoleEligibilityScheduleInstance] = Field(alias="activatedUsing",default=None,)

from .app_scope import AppScope
from .directory_object import DirectoryObject
from .directory_object import DirectoryObject
from .unified_role_definition import UnifiedRoleDefinition
from .unified_role_eligibility_schedule_instance import UnifiedRoleEligibilityScheduleInstance


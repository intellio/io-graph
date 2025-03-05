from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class UnifiedRoleAssignmentScheduleInstance(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	appScopeId: Optional[str] = Field(default=None,alias="appScopeId",)
	directoryScopeId: Optional[str] = Field(default=None,alias="directoryScopeId",)
	principalId: Optional[str] = Field(default=None,alias="principalId",)
	roleDefinitionId: Optional[str] = Field(default=None,alias="roleDefinitionId",)
	appScope: Optional[AppScope] = Field(default=None,alias="appScope",)
	directoryScope: Optional[DirectoryObject] = Field(default=None,alias="directoryScope",)
	principal: Optional[DirectoryObject] = Field(default=None,alias="principal",)
	roleDefinition: Optional[UnifiedRoleDefinition] = Field(default=None,alias="roleDefinition",)
	assignmentType: Optional[str] = Field(default=None,alias="assignmentType",)
	endDateTime: Optional[datetime] = Field(default=None,alias="endDateTime",)
	memberType: Optional[str] = Field(default=None,alias="memberType",)
	roleAssignmentOriginId: Optional[str] = Field(default=None,alias="roleAssignmentOriginId",)
	roleAssignmentScheduleId: Optional[str] = Field(default=None,alias="roleAssignmentScheduleId",)
	startDateTime: Optional[datetime] = Field(default=None,alias="startDateTime",)
	activatedUsing: Optional[UnifiedRoleEligibilityScheduleInstance] = Field(default=None,alias="activatedUsing",)

from .app_scope import AppScope
from .directory_object import DirectoryObject
from .directory_object import DirectoryObject
from .unified_role_definition import UnifiedRoleDefinition
from .unified_role_eligibility_schedule_instance import UnifiedRoleEligibilityScheduleInstance


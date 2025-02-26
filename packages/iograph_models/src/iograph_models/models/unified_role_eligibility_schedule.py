from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class UnifiedRoleEligibilitySchedule(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	appScopeId: Optional[str] = Field(default=None,alias="appScopeId",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	createdUsing: Optional[str] = Field(default=None,alias="createdUsing",)
	directoryScopeId: Optional[str] = Field(default=None,alias="directoryScopeId",)
	modifiedDateTime: Optional[datetime] = Field(default=None,alias="modifiedDateTime",)
	principalId: Optional[str] = Field(default=None,alias="principalId",)
	roleDefinitionId: Optional[str] = Field(default=None,alias="roleDefinitionId",)
	status: Optional[str] = Field(default=None,alias="status",)
	appScope: Optional[AppScope] = Field(default=None,alias="appScope",)
	directoryScope: Optional[DirectoryObject] = Field(default=None,alias="directoryScope",)
	principal: Optional[DirectoryObject] = Field(default=None,alias="principal",)
	roleDefinition: Optional[UnifiedRoleDefinition] = Field(default=None,alias="roleDefinition",)
	memberType: Optional[str] = Field(default=None,alias="memberType",)
	scheduleInfo: Optional[RequestSchedule] = Field(default=None,alias="scheduleInfo",)

from .app_scope import AppScope
from .directory_object import DirectoryObject
from .directory_object import DirectoryObject
from .unified_role_definition import UnifiedRoleDefinition
from .request_schedule import RequestSchedule


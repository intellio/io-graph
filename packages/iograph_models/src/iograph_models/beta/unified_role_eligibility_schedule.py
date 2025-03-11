from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class UnifiedRoleEligibilitySchedule(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	appScopeId: Optional[str] = Field(alias="appScopeId",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	createdUsing: Optional[str] = Field(alias="createdUsing",default=None,)
	directoryScopeId: Optional[str] = Field(alias="directoryScopeId",default=None,)
	modifiedDateTime: Optional[datetime] = Field(alias="modifiedDateTime",default=None,)
	principalId: Optional[str] = Field(alias="principalId",default=None,)
	roleDefinitionId: Optional[str] = Field(alias="roleDefinitionId",default=None,)
	status: Optional[str] = Field(alias="status",default=None,)
	appScope: SerializeAsAny[Optional[AppScope]] = Field(alias="appScope",default=None,)
	directoryScope: SerializeAsAny[Optional[DirectoryObject]] = Field(alias="directoryScope",default=None,)
	principal: SerializeAsAny[Optional[DirectoryObject]] = Field(alias="principal",default=None,)
	roleDefinition: Optional[UnifiedRoleDefinition] = Field(alias="roleDefinition",default=None,)
	memberType: Optional[str] = Field(alias="memberType",default=None,)
	scheduleInfo: Optional[RequestSchedule] = Field(alias="scheduleInfo",default=None,)

from .app_scope import AppScope
from .directory_object import DirectoryObject
from .directory_object import DirectoryObject
from .unified_role_definition import UnifiedRoleDefinition
from .request_schedule import RequestSchedule


from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UnifiedRoleAssignment(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	appScopeId: Optional[str] = Field(default=None,alias="appScopeId",)
	condition: Optional[str] = Field(default=None,alias="condition",)
	directoryScopeId: Optional[str] = Field(default=None,alias="directoryScopeId",)
	principalId: Optional[str] = Field(default=None,alias="principalId",)
	roleDefinitionId: Optional[str] = Field(default=None,alias="roleDefinitionId",)
	appScope: Optional[AppScope] = Field(default=None,alias="appScope",)
	directoryScope: Optional[DirectoryObject] = Field(default=None,alias="directoryScope",)
	principal: Optional[DirectoryObject] = Field(default=None,alias="principal",)
	roleDefinition: Optional[UnifiedRoleDefinition] = Field(default=None,alias="roleDefinition",)

from .app_scope import AppScope
from .directory_object import DirectoryObject
from .directory_object import DirectoryObject
from .unified_role_definition import UnifiedRoleDefinition


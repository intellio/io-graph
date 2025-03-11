from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UnifiedRoleAssignment(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	appScopeId: Optional[str] = Field(alias="appScopeId",default=None,)
	condition: Optional[str] = Field(alias="condition",default=None,)
	directoryScopeId: Optional[str] = Field(alias="directoryScopeId",default=None,)
	principalId: Optional[str] = Field(alias="principalId",default=None,)
	principalOrganizationId: Optional[str] = Field(alias="principalOrganizationId",default=None,)
	resourceScope: Optional[str] = Field(alias="resourceScope",default=None,)
	roleDefinitionId: Optional[str] = Field(alias="roleDefinitionId",default=None,)
	appScope: SerializeAsAny[Optional[AppScope]] = Field(alias="appScope",default=None,)
	directoryScope: SerializeAsAny[Optional[DirectoryObject]] = Field(alias="directoryScope",default=None,)
	principal: SerializeAsAny[Optional[DirectoryObject]] = Field(alias="principal",default=None,)
	roleDefinition: Optional[UnifiedRoleDefinition] = Field(alias="roleDefinition",default=None,)

from .app_scope import AppScope
from .directory_object import DirectoryObject
from .directory_object import DirectoryObject
from .unified_role_definition import UnifiedRoleDefinition


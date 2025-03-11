from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UnifiedRoleAssignmentMultiple(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	appScopeIds: Optional[list[str]] = Field(alias="appScopeIds",default=None,)
	condition: Optional[str] = Field(alias="condition",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	directoryScopeIds: Optional[list[str]] = Field(alias="directoryScopeIds",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	principalIds: Optional[list[str]] = Field(alias="principalIds",default=None,)
	roleDefinitionId: Optional[str] = Field(alias="roleDefinitionId",default=None,)
	appScopes: SerializeAsAny[Optional[list[AppScope]]] = Field(alias="appScopes",default=None,)
	directoryScopes: SerializeAsAny[Optional[list[DirectoryObject]]] = Field(alias="directoryScopes",default=None,)
	principals: SerializeAsAny[Optional[list[DirectoryObject]]] = Field(alias="principals",default=None,)
	roleDefinition: Optional[UnifiedRoleDefinition] = Field(alias="roleDefinition",default=None,)

from .app_scope import AppScope
from .directory_object import DirectoryObject
from .directory_object import DirectoryObject
from .unified_role_definition import UnifiedRoleDefinition


from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UnifiedRoleDefinition(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	allowedPrincipalTypes: Optional[AllowedRolePrincipalTypes | str] = Field(alias="allowedPrincipalTypes",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	isBuiltIn: Optional[bool] = Field(alias="isBuiltIn",default=None,)
	isEnabled: Optional[bool] = Field(alias="isEnabled",default=None,)
	isPrivileged: Optional[bool] = Field(alias="isPrivileged",default=None,)
	resourceScopes: Optional[list[str]] = Field(alias="resourceScopes",default=None,)
	rolePermissions: Optional[list[UnifiedRolePermission]] = Field(alias="rolePermissions",default=None,)
	templateId: Optional[str] = Field(alias="templateId",default=None,)
	version: Optional[str] = Field(alias="version",default=None,)
	inheritsPermissionsFrom: Optional[list[UnifiedRoleDefinition]] = Field(alias="inheritsPermissionsFrom",default=None,)

from .allowed_role_principal_types import AllowedRolePrincipalTypes
from .unified_role_permission import UnifiedRolePermission


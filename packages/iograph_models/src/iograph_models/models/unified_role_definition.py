from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UnifiedRoleDefinition(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	isBuiltIn: Optional[bool] = Field(default=None,alias="isBuiltIn",)
	isEnabled: Optional[bool] = Field(default=None,alias="isEnabled",)
	resourceScopes: Optional[list[str]] = Field(default=None,alias="resourceScopes",)
	rolePermissions: Optional[list[UnifiedRolePermission]] = Field(default=None,alias="rolePermissions",)
	templateId: Optional[str] = Field(default=None,alias="templateId",)
	version: Optional[str] = Field(default=None,alias="version",)
	inheritsPermissionsFrom: Optional[list[UnifiedRoleDefinition]] = Field(default=None,alias="inheritsPermissionsFrom",)

from .unified_role_permission import UnifiedRolePermission


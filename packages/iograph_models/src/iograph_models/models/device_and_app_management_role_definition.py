from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DeviceAndAppManagementRoleDefinition(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	isBuiltIn: Optional[bool] = Field(default=None,alias="isBuiltIn",)
	rolePermissions: list[RolePermission] = Field(alias="rolePermissions",)
	roleAssignments: list[RoleAssignment] = Field(alias="roleAssignments",)

from .role_permission import RolePermission
from .role_assignment import RoleAssignment


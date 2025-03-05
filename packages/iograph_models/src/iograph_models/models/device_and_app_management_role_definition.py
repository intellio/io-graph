from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceAndAppManagementRoleDefinition(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	isBuiltIn: Optional[bool] = Field(alias="isBuiltIn",default=None,)
	rolePermissions: Optional[list[RolePermission]] = Field(alias="rolePermissions",default=None,)
	roleAssignments: SerializeAsAny[Optional[list[RoleAssignment]]] = Field(alias="roleAssignments",default=None,)

from .role_permission import RolePermission
from .role_assignment import RoleAssignment


from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceAndAppManagementRoleDefinition(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.deviceAndAppManagementRoleDefinition"] = Field(alias="@odata.type", default="#microsoft.graph.deviceAndAppManagementRoleDefinition")
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	isBuiltIn: Optional[bool] = Field(alias="isBuiltIn", default=None,)
	rolePermissions: Optional[list[RolePermission]] = Field(alias="rolePermissions", default=None,)
	roleAssignments: Optional[list[Annotated[Union[DeviceAndAppManagementRoleAssignment]],Field(discriminator="odata_type")]]] = Field(alias="roleAssignments", default=None,)

from .role_permission import RolePermission
from .device_and_app_management_role_assignment import DeviceAndAppManagementRoleAssignment


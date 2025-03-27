from __future__ import annotations
from typing import Optional
from typing import Union
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceAndAppManagementRoleAssignment(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	resourceScopes: Optional[list[str]] = Field(alias="resourceScopes", default=None,)
	scopeMembers: Optional[list[str]] = Field(alias="scopeMembers", default=None,)
	scopeType: Optional[RoleAssignmentScopeType | str] = Field(alias="scopeType", default=None,)
	roleDefinition: Optional[Union[DeviceAndAppManagementRoleDefinition]] = Field(alias="roleDefinition", default=None,discriminator="odata_type", )
	members: Optional[list[str]] = Field(alias="members", default=None,)
	roleScopeTags: Optional[list[RoleScopeTag]] = Field(alias="roleScopeTags", default=None,)

from .role_assignment_scope_type import RoleAssignmentScopeType
from .device_and_app_management_role_definition import DeviceAndAppManagementRoleDefinition
from .role_scope_tag import RoleScopeTag


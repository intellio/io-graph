from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceAndAppManagementRoleAssignment(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	resourceScopes: Optional[list[str]] = Field(default=None,alias="resourceScopes",)
	roleDefinition: Optional[RoleDefinition] = Field(default=None,alias="roleDefinition",)
	members: Optional[list[str]] = Field(default=None,alias="members",)

from .role_definition import RoleDefinition


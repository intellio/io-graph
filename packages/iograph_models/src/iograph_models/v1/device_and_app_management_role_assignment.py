from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import BaseModel, Field


class DeviceAndAppManagementRoleAssignment(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.deviceAndAppManagementRoleAssignment"] = Field(alias="@odata.type", default="#microsoft.graph.deviceAndAppManagementRoleAssignment")
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	resourceScopes: Optional[list[str]] = Field(alias="resourceScopes", default=None,)
	roleDefinition: Optional[Union[DeviceAndAppManagementRoleDefinition]] = Field(alias="roleDefinition", default=None,discriminator="odata_type", )
	members: Optional[list[str]] = Field(alias="members", default=None,)

from .device_and_app_management_role_definition import DeviceAndAppManagementRoleDefinition

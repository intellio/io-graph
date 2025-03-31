from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DeviceAndAppManagementAssignedRoleDetail(BaseModel):
	permissions: Optional[list[str]] = Field(alias="permissions", default=None,)
	roleDefinitions: Optional[list[DeviceAndAppManagementAssignedRoleDefinition]] = Field(alias="roleDefinitions", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .device_and_app_management_assigned_role_definition import DeviceAndAppManagementAssignedRoleDefinition

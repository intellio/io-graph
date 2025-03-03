from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DeviceAndAppManagementRoleAssignmentCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[DeviceAndAppManagementRoleAssignment]] = Field(default=None,alias="value",)

from .device_and_app_management_role_assignment import DeviceAndAppManagementRoleAssignment


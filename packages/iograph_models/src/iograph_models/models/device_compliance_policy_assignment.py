from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DeviceCompliancePolicyAssignment(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	target: Optional[DeviceAndAppManagementAssignmentTarget] = Field(default=None,alias="target",)

from .device_and_app_management_assignment_target import DeviceAndAppManagementAssignmentTarget


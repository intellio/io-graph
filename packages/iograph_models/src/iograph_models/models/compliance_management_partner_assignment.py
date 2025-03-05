from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ComplianceManagementPartnerAssignment(BaseModel):
	target: SerializeAsAny[Optional[DeviceAndAppManagementAssignmentTarget]] = Field(default=None,alias="target",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .device_and_app_management_assignment_target import DeviceAndAppManagementAssignmentTarget


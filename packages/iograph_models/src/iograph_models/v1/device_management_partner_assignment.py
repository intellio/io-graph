from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementPartnerAssignment(BaseModel):
	target: SerializeAsAny[Optional[DeviceAndAppManagementAssignmentTarget]] = Field(alias="target",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .device_and_app_management_assignment_target import DeviceAndAppManagementAssignmentTarget


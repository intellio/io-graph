from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Validate_filterPostRequest(BaseModel):
	deviceAndAppManagementAssignmentFilter: SerializeAsAny[Optional[DeviceAndAppManagementAssignmentFilter]] = Field(alias="deviceAndAppManagementAssignmentFilter",default=None,)

from .device_and_app_management_assignment_filter import DeviceAndAppManagementAssignmentFilter


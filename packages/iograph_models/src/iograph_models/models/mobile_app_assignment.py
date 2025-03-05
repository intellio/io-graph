from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MobileAppAssignment(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	intent: Optional[InstallIntent] = Field(default=None,alias="intent",)
	settings: SerializeAsAny[Optional[MobileAppAssignmentSettings]] = Field(default=None,alias="settings",)
	target: SerializeAsAny[Optional[DeviceAndAppManagementAssignmentTarget]] = Field(default=None,alias="target",)

from .install_intent import InstallIntent
from .mobile_app_assignment_settings import MobileAppAssignmentSettings
from .device_and_app_management_assignment_target import DeviceAndAppManagementAssignmentTarget


from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MobileAppAssignment(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	intent: Optional[InstallIntent | str] = Field(alias="intent",default=None,)
	settings: SerializeAsAny[Optional[MobileAppAssignmentSettings]] = Field(alias="settings",default=None,)
	target: SerializeAsAny[Optional[DeviceAndAppManagementAssignmentTarget]] = Field(alias="target",default=None,)

from .install_intent import InstallIntent
from .mobile_app_assignment_settings import MobileAppAssignmentSettings
from .device_and_app_management_assignment_target import DeviceAndAppManagementAssignmentTarget


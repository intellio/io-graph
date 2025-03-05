from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IosVppEBookAssignment(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	installIntent: Optional[InstallIntent] = Field(default=None,alias="installIntent",)
	target: SerializeAsAny[Optional[DeviceAndAppManagementAssignmentTarget]] = Field(default=None,alias="target",)

from .install_intent import InstallIntent
from .device_and_app_management_assignment_target import DeviceAndAppManagementAssignmentTarget


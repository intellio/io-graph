from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IosVppEBookAssignment(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	installIntent: Optional[InstallIntent | str] = Field(alias="installIntent",default=None,)
	target: SerializeAsAny[Optional[DeviceAndAppManagementAssignmentTarget]] = Field(alias="target",default=None,)

from .install_intent import InstallIntent
from .device_and_app_management_assignment_target import DeviceAndAppManagementAssignmentTarget


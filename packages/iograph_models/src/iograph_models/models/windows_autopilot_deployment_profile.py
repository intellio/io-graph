from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsAutopilotDeploymentProfile(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	deviceNameTemplate: Optional[str] = Field(default=None,alias="deviceNameTemplate",)
	deviceType: Optional[WindowsAutopilotDeviceType] = Field(default=None,alias="deviceType",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	hardwareHashExtractionEnabled: Optional[bool] = Field(default=None,alias="hardwareHashExtractionEnabled",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	locale: Optional[str] = Field(default=None,alias="locale",)
	managementServiceAppId: Optional[str] = Field(default=None,alias="managementServiceAppId",)
	outOfBoxExperienceSetting: Optional[OutOfBoxExperienceSetting] = Field(default=None,alias="outOfBoxExperienceSetting",)
	preprovisioningAllowed: Optional[bool] = Field(default=None,alias="preprovisioningAllowed",)
	roleScopeTagIds: Optional[list[str]] = Field(default=None,alias="roleScopeTagIds",)
	assignedDevices: Optional[list[WindowsAutopilotDeviceIdentity]] = Field(default=None,alias="assignedDevices",)

from .windows_autopilot_device_type import WindowsAutopilotDeviceType
from .out_of_box_experience_setting import OutOfBoxExperienceSetting
from .windows_autopilot_device_identity import WindowsAutopilotDeviceIdentity


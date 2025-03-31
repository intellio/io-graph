from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class WindowsAutopilotDeploymentProfile(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.windowsAutopilotDeploymentProfile"] = Field(alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	deviceNameTemplate: Optional[str] = Field(alias="deviceNameTemplate", default=None,)
	deviceType: Optional[WindowsAutopilotDeviceType | str] = Field(alias="deviceType", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	hardwareHashExtractionEnabled: Optional[bool] = Field(alias="hardwareHashExtractionEnabled", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	locale: Optional[str] = Field(alias="locale", default=None,)
	managementServiceAppId: Optional[str] = Field(alias="managementServiceAppId", default=None,)
	outOfBoxExperienceSetting: Optional[OutOfBoxExperienceSetting] = Field(alias="outOfBoxExperienceSetting", default=None,)
	preprovisioningAllowed: Optional[bool] = Field(alias="preprovisioningAllowed", default=None,)
	roleScopeTagIds: Optional[list[str]] = Field(alias="roleScopeTagIds", default=None,)
	assignedDevices: Optional[list[WindowsAutopilotDeviceIdentity]] = Field(alias="assignedDevices", default=None,)

from .windows_autopilot_device_type import WindowsAutopilotDeviceType
from .out_of_box_experience_setting import OutOfBoxExperienceSetting
from .windows_autopilot_device_identity import WindowsAutopilotDeviceIdentity

from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ActiveDirectoryWindowsAutopilotDeploymentProfile(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.activeDirectoryWindowsAutopilotDeploymentProfile"] = Field(alias="@odata.type", default="#microsoft.graph.activeDirectoryWindowsAutopilotDeploymentProfile")
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	deviceNameTemplate: Optional[str] = Field(alias="deviceNameTemplate", default=None,)
	deviceType: Optional[WindowsAutopilotDeviceType | str] = Field(alias="deviceType", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	enableWhiteGlove: Optional[bool] = Field(alias="enableWhiteGlove", default=None,)
	enrollmentStatusScreenSettings: Optional[WindowsEnrollmentStatusScreenSettings] = Field(alias="enrollmentStatusScreenSettings", default=None,)
	extractHardwareHash: Optional[bool] = Field(alias="extractHardwareHash", default=None,)
	hardwareHashExtractionEnabled: Optional[bool] = Field(alias="hardwareHashExtractionEnabled", default=None,)
	language: Optional[str] = Field(alias="language", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	locale: Optional[str] = Field(alias="locale", default=None,)
	managementServiceAppId: Optional[str] = Field(alias="managementServiceAppId", default=None,)
	outOfBoxExperienceSetting: Optional[OutOfBoxExperienceSetting] = Field(alias="outOfBoxExperienceSetting", default=None,)
	outOfBoxExperienceSettings: Optional[OutOfBoxExperienceSettings] = Field(alias="outOfBoxExperienceSettings", default=None,)
	preprovisioningAllowed: Optional[bool] = Field(alias="preprovisioningAllowed", default=None,)
	roleScopeTagIds: Optional[list[str]] = Field(alias="roleScopeTagIds", default=None,)
	assignedDevices: Optional[list[WindowsAutopilotDeviceIdentity]] = Field(alias="assignedDevices", default=None,)
	assignments: Optional[list[WindowsAutopilotDeploymentProfileAssignment]] = Field(alias="assignments", default=None,)
	hybridAzureADJoinSkipConnectivityCheck: Optional[bool] = Field(alias="hybridAzureADJoinSkipConnectivityCheck", default=None,)
	domainJoinConfiguration: Optional[WindowsDomainJoinConfiguration] = Field(alias="domainJoinConfiguration", default=None,)

from .windows_autopilot_device_type import WindowsAutopilotDeviceType
from .windows_enrollment_status_screen_settings import WindowsEnrollmentStatusScreenSettings
from .out_of_box_experience_setting import OutOfBoxExperienceSetting
from .out_of_box_experience_settings import OutOfBoxExperienceSettings
from .windows_autopilot_device_identity import WindowsAutopilotDeviceIdentity
from .windows_autopilot_deployment_profile_assignment import WindowsAutopilotDeploymentProfileAssignment
from .windows_domain_join_configuration import WindowsDomainJoinConfiguration


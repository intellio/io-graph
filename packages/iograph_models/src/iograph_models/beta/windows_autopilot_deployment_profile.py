from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class WindowsAutopilotDeploymentProfile(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
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

	@model_validator(mode="wrap")
	def convert_discriminator_class(cls, data: Any, handler: ModelWrapValidatorHandler[Self]) -> Self:
		try:
			# check with parent model to catch any errors
			parent_validated_model = handler(data)
			# check if the discriminator field is present
			if "@odata.type" not in data:
				return parent_validated_model
			# get the discriminator value
			mapping_key = data["@odata.type"]
			if mapping_key == "#microsoft.graph.activeDirectoryWindowsAutopilotDeploymentProfile":
				from .active_directory_windows_autopilot_deployment_profile import ActiveDirectoryWindowsAutopilotDeploymentProfile
				return ActiveDirectoryWindowsAutopilotDeploymentProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.azureADWindowsAutopilotDeploymentProfile":
				from .azure_a_d_windows_autopilot_deployment_profile import AzureADWindowsAutopilotDeploymentProfile
				return AzureADWindowsAutopilotDeploymentProfile.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .windows_autopilot_device_type import WindowsAutopilotDeviceType
from .windows_enrollment_status_screen_settings import WindowsEnrollmentStatusScreenSettings
from .out_of_box_experience_setting import OutOfBoxExperienceSetting
from .out_of_box_experience_settings import OutOfBoxExperienceSettings
from .windows_autopilot_device_identity import WindowsAutopilotDeviceIdentity
from .windows_autopilot_deployment_profile_assignment import WindowsAutopilotDeploymentProfileAssignment

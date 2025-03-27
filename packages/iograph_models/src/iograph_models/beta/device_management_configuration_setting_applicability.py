from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementConfigurationSettingApplicability(BaseModel):
	description: Optional[str] = Field(alias="description", default=None,)
	deviceMode: Optional[DeviceManagementConfigurationDeviceMode | str] = Field(alias="deviceMode", default=None,)
	platform: Optional[DeviceManagementConfigurationPlatforms | str] = Field(alias="platform", default=None,)
	technologies: Optional[DeviceManagementConfigurationTechnologies | str] = Field(alias="technologies", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

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
			if mapping_key == "#microsoft.graph.deviceManagementConfigurationApplicationSettingApplicability":
				from .device_management_configuration_application_setting_applicability import DeviceManagementConfigurationApplicationSettingApplicability
				return DeviceManagementConfigurationApplicationSettingApplicability.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementConfigurationExchangeOnlineSettingApplicability":
				from .device_management_configuration_exchange_online_setting_applicability import DeviceManagementConfigurationExchangeOnlineSettingApplicability
				return DeviceManagementConfigurationExchangeOnlineSettingApplicability.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementConfigurationWindowsSettingApplicability":
				from .device_management_configuration_windows_setting_applicability import DeviceManagementConfigurationWindowsSettingApplicability
				return DeviceManagementConfigurationWindowsSettingApplicability.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .device_management_configuration_device_mode import DeviceManagementConfigurationDeviceMode
from .device_management_configuration_platforms import DeviceManagementConfigurationPlatforms
from .device_management_configuration_technologies import DeviceManagementConfigurationTechnologies


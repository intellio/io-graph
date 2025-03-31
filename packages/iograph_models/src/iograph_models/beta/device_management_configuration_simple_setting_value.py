from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class DeviceManagementConfigurationSimpleSettingValue(BaseModel):
	settingValueTemplateReference: Optional[DeviceManagementConfigurationSettingValueTemplateReference] = Field(alias="settingValueTemplateReference", default=None,)
	odata_type: Literal["#microsoft.graph.deviceManagementConfigurationSimpleSettingValue"] = Field(alias="@odata.type", default="#microsoft.graph.deviceManagementConfigurationSimpleSettingValue")

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
			if mapping_key == "#microsoft.graph.deviceManagementConfigurationIntegerSettingValue":
				from .device_management_configuration_integer_setting_value import DeviceManagementConfigurationIntegerSettingValue
				return DeviceManagementConfigurationIntegerSettingValue.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementConfigurationSecretSettingValue":
				from .device_management_configuration_secret_setting_value import DeviceManagementConfigurationSecretSettingValue
				return DeviceManagementConfigurationSecretSettingValue.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementConfigurationReferenceSettingValue":
				from .device_management_configuration_reference_setting_value import DeviceManagementConfigurationReferenceSettingValue
				return DeviceManagementConfigurationReferenceSettingValue.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .device_management_configuration_setting_value_template_reference import DeviceManagementConfigurationSettingValueTemplateReference

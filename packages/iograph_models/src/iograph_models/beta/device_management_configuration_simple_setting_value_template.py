from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementConfigurationSimpleSettingValueTemplate(BaseModel):
	settingValueTemplateId: Optional[str] = Field(alias="settingValueTemplateId",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

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
			if mapping_key == "#microsoft.graph.deviceManagementConfigurationIntegerSettingValueTemplate":
				from .device_management_configuration_integer_setting_value_template import DeviceManagementConfigurationIntegerSettingValueTemplate
				return DeviceManagementConfigurationIntegerSettingValueTemplate.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementConfigurationStringSettingValueTemplate":
				from .device_management_configuration_string_setting_value_template import DeviceManagementConfigurationStringSettingValueTemplate
				return DeviceManagementConfigurationStringSettingValueTemplate.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e



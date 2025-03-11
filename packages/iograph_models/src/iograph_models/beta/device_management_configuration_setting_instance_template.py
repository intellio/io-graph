from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementConfigurationSettingInstanceTemplate(BaseModel):
	isRequired: Optional[bool] = Field(alias="isRequired",default=None,)
	settingDefinitionId: Optional[str] = Field(alias="settingDefinitionId",default=None,)
	settingInstanceTemplateId: Optional[str] = Field(alias="settingInstanceTemplateId",default=None,)
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
			if mapping_key == "#microsoft.graph.deviceManagementConfigurationChoiceSettingCollectionInstanceTemplate":
				from .device_management_configuration_choice_setting_collection_instance_template import DeviceManagementConfigurationChoiceSettingCollectionInstanceTemplate
				return DeviceManagementConfigurationChoiceSettingCollectionInstanceTemplate.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementConfigurationChoiceSettingInstanceTemplate":
				from .device_management_configuration_choice_setting_instance_template import DeviceManagementConfigurationChoiceSettingInstanceTemplate
				return DeviceManagementConfigurationChoiceSettingInstanceTemplate.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementConfigurationGroupSettingCollectionInstanceTemplate":
				from .device_management_configuration_group_setting_collection_instance_template import DeviceManagementConfigurationGroupSettingCollectionInstanceTemplate
				return DeviceManagementConfigurationGroupSettingCollectionInstanceTemplate.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementConfigurationGroupSettingInstanceTemplate":
				from .device_management_configuration_group_setting_instance_template import DeviceManagementConfigurationGroupSettingInstanceTemplate
				return DeviceManagementConfigurationGroupSettingInstanceTemplate.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementConfigurationSimpleSettingCollectionInstanceTemplate":
				from .device_management_configuration_simple_setting_collection_instance_template import DeviceManagementConfigurationSimpleSettingCollectionInstanceTemplate
				return DeviceManagementConfigurationSimpleSettingCollectionInstanceTemplate.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementConfigurationSimpleSettingInstanceTemplate":
				from .device_management_configuration_simple_setting_instance_template import DeviceManagementConfigurationSimpleSettingInstanceTemplate
				return DeviceManagementConfigurationSimpleSettingInstanceTemplate.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e



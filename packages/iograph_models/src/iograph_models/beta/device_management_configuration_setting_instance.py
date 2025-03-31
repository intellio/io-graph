from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class DeviceManagementConfigurationSettingInstance(BaseModel):
	settingDefinitionId: Optional[str] = Field(alias="settingDefinitionId", default=None,)
	settingInstanceTemplateReference: Optional[DeviceManagementConfigurationSettingInstanceTemplateReference] = Field(alias="settingInstanceTemplateReference", default=None,)
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
			if mapping_key == "#microsoft.graph.deviceManagementConfigurationChoiceSettingCollectionInstance":
				from .device_management_configuration_choice_setting_collection_instance import DeviceManagementConfigurationChoiceSettingCollectionInstance
				return DeviceManagementConfigurationChoiceSettingCollectionInstance.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementConfigurationChoiceSettingInstance":
				from .device_management_configuration_choice_setting_instance import DeviceManagementConfigurationChoiceSettingInstance
				return DeviceManagementConfigurationChoiceSettingInstance.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementConfigurationGroupSettingCollectionInstance":
				from .device_management_configuration_group_setting_collection_instance import DeviceManagementConfigurationGroupSettingCollectionInstance
				return DeviceManagementConfigurationGroupSettingCollectionInstance.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementConfigurationGroupSettingInstance":
				from .device_management_configuration_group_setting_instance import DeviceManagementConfigurationGroupSettingInstance
				return DeviceManagementConfigurationGroupSettingInstance.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementConfigurationSettingGroupCollectionInstance":
				from .device_management_configuration_setting_group_collection_instance import DeviceManagementConfigurationSettingGroupCollectionInstance
				return DeviceManagementConfigurationSettingGroupCollectionInstance.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementConfigurationSettingGroupInstance":
				from .device_management_configuration_setting_group_instance import DeviceManagementConfigurationSettingGroupInstance
				return DeviceManagementConfigurationSettingGroupInstance.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementConfigurationSimpleSettingCollectionInstance":
				from .device_management_configuration_simple_setting_collection_instance import DeviceManagementConfigurationSimpleSettingCollectionInstance
				return DeviceManagementConfigurationSimpleSettingCollectionInstance.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementConfigurationSimpleSettingInstance":
				from .device_management_configuration_simple_setting_instance import DeviceManagementConfigurationSimpleSettingInstance
				return DeviceManagementConfigurationSimpleSettingInstance.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .device_management_configuration_setting_instance_template_reference import DeviceManagementConfigurationSettingInstanceTemplateReference

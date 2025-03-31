from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class DeviceManagementSettingInstance(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	definitionId: Optional[str] = Field(alias="definitionId", default=None,)
	valueJson: Optional[str] = Field(alias="valueJson", default=None,)

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
			if mapping_key == "#microsoft.graph.deviceManagementAbstractComplexSettingInstance":
				from .device_management_abstract_complex_setting_instance import DeviceManagementAbstractComplexSettingInstance
				return DeviceManagementAbstractComplexSettingInstance.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementBooleanSettingInstance":
				from .device_management_boolean_setting_instance import DeviceManagementBooleanSettingInstance
				return DeviceManagementBooleanSettingInstance.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementCollectionSettingInstance":
				from .device_management_collection_setting_instance import DeviceManagementCollectionSettingInstance
				return DeviceManagementCollectionSettingInstance.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementComplexSettingInstance":
				from .device_management_complex_setting_instance import DeviceManagementComplexSettingInstance
				return DeviceManagementComplexSettingInstance.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementIntegerSettingInstance":
				from .device_management_integer_setting_instance import DeviceManagementIntegerSettingInstance
				return DeviceManagementIntegerSettingInstance.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementStringSettingInstance":
				from .device_management_string_setting_instance import DeviceManagementStringSettingInstance
				return DeviceManagementStringSettingInstance.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e


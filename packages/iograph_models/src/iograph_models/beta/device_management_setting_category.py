from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementSettingCategory(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	hasRequiredSetting: Optional[bool] = Field(alias="hasRequiredSetting", default=None,)
	settingDefinitions: Optional[list[Annotated[Union[DeviceManagementAbstractComplexSettingDefinition, DeviceManagementCollectionSettingDefinition, DeviceManagementComplexSettingDefinition],Field(discriminator="odata_type")]]] = Field(alias="settingDefinitions", default=None,)

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
			if mapping_key == "#microsoft.graph.deviceManagementIntentSettingCategory":
				from .device_management_intent_setting_category import DeviceManagementIntentSettingCategory
				return DeviceManagementIntentSettingCategory.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementTemplateSettingCategory":
				from .device_management_template_setting_category import DeviceManagementTemplateSettingCategory
				return DeviceManagementTemplateSettingCategory.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .device_management_abstract_complex_setting_definition import DeviceManagementAbstractComplexSettingDefinition
from .device_management_collection_setting_definition import DeviceManagementCollectionSettingDefinition
from .device_management_complex_setting_definition import DeviceManagementComplexSettingDefinition


from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementSettingDefinition(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	constraints: SerializeAsAny[Optional[list[DeviceManagementConstraint]]] = Field(alias="constraints",default=None,)
	dependencies: Optional[list[DeviceManagementSettingDependency]] = Field(alias="dependencies",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	documentationUrl: Optional[str] = Field(alias="documentationUrl",default=None,)
	headerSubtitle: Optional[str] = Field(alias="headerSubtitle",default=None,)
	headerTitle: Optional[str] = Field(alias="headerTitle",default=None,)
	isTopLevel: Optional[bool] = Field(alias="isTopLevel",default=None,)
	keywords: Optional[list[str]] = Field(alias="keywords",default=None,)
	placeholderText: Optional[str] = Field(alias="placeholderText",default=None,)
	valueType: Optional[DeviceManangementIntentValueType | str] = Field(alias="valueType",default=None,)

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
			if mapping_key == "#microsoft.graph.deviceManagementAbstractComplexSettingDefinition":
				from .device_management_abstract_complex_setting_definition import DeviceManagementAbstractComplexSettingDefinition
				return DeviceManagementAbstractComplexSettingDefinition.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementCollectionSettingDefinition":
				from .device_management_collection_setting_definition import DeviceManagementCollectionSettingDefinition
				return DeviceManagementCollectionSettingDefinition.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementComplexSettingDefinition":
				from .device_management_complex_setting_definition import DeviceManagementComplexSettingDefinition
				return DeviceManagementComplexSettingDefinition.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .device_management_constraint import DeviceManagementConstraint
from .device_management_setting_dependency import DeviceManagementSettingDependency
from .device_manangement_intent_value_type import DeviceManangementIntentValueType


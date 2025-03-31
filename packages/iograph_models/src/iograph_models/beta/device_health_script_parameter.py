from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class DeviceHealthScriptParameter(BaseModel):
	applyDefaultValueWhenNotAssigned: Optional[bool] = Field(alias="applyDefaultValueWhenNotAssigned", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	isRequired: Optional[bool] = Field(alias="isRequired", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
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
			if mapping_key == "#microsoft.graph.deviceHealthScriptBooleanParameter":
				from .device_health_script_boolean_parameter import DeviceHealthScriptBooleanParameter
				return DeviceHealthScriptBooleanParameter.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceHealthScriptIntegerParameter":
				from .device_health_script_integer_parameter import DeviceHealthScriptIntegerParameter
				return DeviceHealthScriptIntegerParameter.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceHealthScriptStringParameter":
				from .device_health_script_string_parameter import DeviceHealthScriptStringParameter
				return DeviceHealthScriptStringParameter.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e


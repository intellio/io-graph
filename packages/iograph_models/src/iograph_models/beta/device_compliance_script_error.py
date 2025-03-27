from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceComplianceScriptError(BaseModel):
	code: Optional[Code | str] = Field(alias="code", default=None,)
	deviceComplianceScriptRulesValidationError: Optional[DeviceComplianceScriptRulesValidationError | str] = Field(alias="deviceComplianceScriptRulesValidationError", default=None,)
	message: Optional[str] = Field(alias="message", default=None,)
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
			if mapping_key == "#microsoft.graph.deviceComplianceScriptRuleError":
				from .device_compliance_script_rule_error import DeviceComplianceScriptRuleError
				return DeviceComplianceScriptRuleError.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .code import Code
from .device_compliance_script_rules_validation_error import DeviceComplianceScriptRulesValidationError


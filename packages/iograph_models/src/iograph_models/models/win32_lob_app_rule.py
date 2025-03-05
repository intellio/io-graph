from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from pydantic import BaseModel, Field, SerializeAsAny


class Win32LobAppRule(BaseModel):
	ruleType: Optional[str | Win32LobAppRuleType] = Field(alias="ruleType",default=None,)
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
			if mapping_key == "#microsoft.graph.win32LobAppFileSystemRule":
				from .win32_lob_app_file_system_rule import Win32LobAppFileSystemRule
				return Win32LobAppFileSystemRule.model_validate(data)
			if mapping_key == "#microsoft.graph.win32LobAppPowerShellScriptRule":
				from .win32_lob_app_power_shell_script_rule import Win32LobAppPowerShellScriptRule
				return Win32LobAppPowerShellScriptRule.model_validate(data)
			if mapping_key == "#microsoft.graph.win32LobAppProductCodeRule":
				from .win32_lob_app_product_code_rule import Win32LobAppProductCodeRule
				return Win32LobAppProductCodeRule.model_validate(data)
			if mapping_key == "#microsoft.graph.win32LobAppRegistryRule":
				from .win32_lob_app_registry_rule import Win32LobAppRegistryRule
				return Win32LobAppRegistryRule.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .win32_lob_app_rule_type import Win32LobAppRuleType


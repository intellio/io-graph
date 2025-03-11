from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class Win32LobAppDetection(BaseModel):
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
			if mapping_key == "#microsoft.graph.win32LobAppFileSystemDetection":
				from .win32_lob_app_file_system_detection import Win32LobAppFileSystemDetection
				return Win32LobAppFileSystemDetection.model_validate(data)
			if mapping_key == "#microsoft.graph.win32LobAppPowerShellScriptDetection":
				from .win32_lob_app_power_shell_script_detection import Win32LobAppPowerShellScriptDetection
				return Win32LobAppPowerShellScriptDetection.model_validate(data)
			if mapping_key == "#microsoft.graph.win32LobAppProductCodeDetection":
				from .win32_lob_app_product_code_detection import Win32LobAppProductCodeDetection
				return Win32LobAppProductCodeDetection.model_validate(data)
			if mapping_key == "#microsoft.graph.win32LobAppRegistryDetection":
				from .win32_lob_app_registry_detection import Win32LobAppRegistryDetection
				return Win32LobAppRegistryDetection.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e



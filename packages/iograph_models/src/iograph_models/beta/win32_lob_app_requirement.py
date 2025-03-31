from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class Win32LobAppRequirement(BaseModel):
	detectionValue: Optional[str] = Field(alias="detectionValue", default=None,)
	operator: Optional[Win32LobAppDetectionOperator | str] = Field(alias="operator", default=None,)
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
			if mapping_key == "#microsoft.graph.win32LobAppFileSystemRequirement":
				from .win32_lob_app_file_system_requirement import Win32LobAppFileSystemRequirement
				return Win32LobAppFileSystemRequirement.model_validate(data)
			if mapping_key == "#microsoft.graph.win32LobAppPowerShellScriptRequirement":
				from .win32_lob_app_power_shell_script_requirement import Win32LobAppPowerShellScriptRequirement
				return Win32LobAppPowerShellScriptRequirement.model_validate(data)
			if mapping_key == "#microsoft.graph.win32LobAppRegistryRequirement":
				from .win32_lob_app_registry_requirement import Win32LobAppRegistryRequirement
				return Win32LobAppRegistryRequirement.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .win32_lob_app_detection_operator import Win32LobAppDetectionOperator

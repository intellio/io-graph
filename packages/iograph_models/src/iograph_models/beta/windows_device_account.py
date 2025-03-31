from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class WindowsDeviceAccount(BaseModel):
	password: Optional[str] = Field(alias="password", default=None,)
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
			if mapping_key == "#microsoft.graph.windowsDeviceADAccount":
				from .windows_device_a_d_account import WindowsDeviceADAccount
				return WindowsDeviceADAccount.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsDeviceAzureADAccount":
				from .windows_device_azure_a_d_account import WindowsDeviceAzureADAccount
				return WindowsDeviceAzureADAccount.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e


from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class AuthenticationMethodDevice(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	hardwareOathDevices: Optional[list[HardwareOathTokenAuthenticationMethodDevice]] = Field(alias="hardwareOathDevices", default=None,)

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
			if mapping_key == "#microsoft.graph.hardwareOathTokenAuthenticationMethodDevice":
				from .hardware_oath_token_authentication_method_device import HardwareOathTokenAuthenticationMethodDevice
				return HardwareOathTokenAuthenticationMethodDevice.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .hardware_oath_token_authentication_method_device import HardwareOathTokenAuthenticationMethodDevice

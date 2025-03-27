from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class VpnProxyServer(BaseModel):
	address: Optional[str] = Field(alias="address", default=None,)
	automaticConfigurationScriptUrl: Optional[str] = Field(alias="automaticConfigurationScriptUrl", default=None,)
	port: Optional[int] = Field(alias="port", default=None,)
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
			if mapping_key == "#microsoft.graph.windows10VpnProxyServer":
				from .windows10_vpn_proxy_server import Windows10VpnProxyServer
				return Windows10VpnProxyServer.model_validate(data)
			if mapping_key == "#microsoft.graph.windows81VpnProxyServer":
				from .windows81_vpn_proxy_server import Windows81VpnProxyServer
				return Windows81VpnProxyServer.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e



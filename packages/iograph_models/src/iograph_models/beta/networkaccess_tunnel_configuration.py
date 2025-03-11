from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessTunnelConfiguration(BaseModel):
	preSharedKey: Optional[str] = Field(alias="preSharedKey",default=None,)
	zoneRedundancyPreSharedKey: Optional[str] = Field(alias="zoneRedundancyPreSharedKey",default=None,)
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
			if mapping_key == "#microsoft.graph.networkaccess.tunnelConfigurationIKEv2Custom":
				from .networkaccess_tunnel_configuration_i_k_ev2_custom import NetworkaccessTunnelConfigurationIKEv2Custom
				return NetworkaccessTunnelConfigurationIKEv2Custom.model_validate(data)
			if mapping_key == "#microsoft.graph.networkaccess.tunnelConfigurationIKEv2Default":
				from .networkaccess_tunnel_configuration_i_k_ev2_default import NetworkaccessTunnelConfigurationIKEv2Default
				return NetworkaccessTunnelConfigurationIKEv2Default.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e



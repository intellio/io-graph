from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class NetworkaccessRuleDestination(BaseModel):
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
			if mapping_key == "#microsoft.graph.networkaccess.fqdn":
				from .networkaccess_fqdn import NetworkaccessFqdn
				return NetworkaccessFqdn.model_validate(data)
			if mapping_key == "#microsoft.graph.networkaccess.ipAddress":
				from .networkaccess_ip_address import NetworkaccessIpAddress
				return NetworkaccessIpAddress.model_validate(data)
			if mapping_key == "#microsoft.graph.networkaccess.ipRange":
				from .networkaccess_ip_range import NetworkaccessIpRange
				return NetworkaccessIpRange.model_validate(data)
			if mapping_key == "#microsoft.graph.networkaccess.ipSubnet":
				from .networkaccess_ip_subnet import NetworkaccessIpSubnet
				return NetworkaccessIpSubnet.model_validate(data)
			if mapping_key == "#microsoft.graph.networkaccess.url":
				from .networkaccess_url import NetworkaccessUrl
				return NetworkaccessUrl.model_validate(data)
			if mapping_key == "#microsoft.graph.networkaccess.webCategory":
				from .networkaccess_web_category import NetworkaccessWebCategory
				return NetworkaccessWebCategory.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e


from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class NetworkaccessPolicyRule(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)

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
			if mapping_key == "#microsoft.graph.networkaccess.fqdnFilteringRule":
				from .networkaccess_fqdn_filtering_rule import NetworkaccessFqdnFilteringRule
				return NetworkaccessFqdnFilteringRule.model_validate(data)
			if mapping_key == "#microsoft.graph.networkaccess.webCategoryFilteringRule":
				from .networkaccess_web_category_filtering_rule import NetworkaccessWebCategoryFilteringRule
				return NetworkaccessWebCategoryFilteringRule.model_validate(data)
			if mapping_key == "#microsoft.graph.networkaccess.internetAccessForwardingRule":
				from .networkaccess_internet_access_forwarding_rule import NetworkaccessInternetAccessForwardingRule
				return NetworkaccessInternetAccessForwardingRule.model_validate(data)
			if mapping_key == "#microsoft.graph.networkaccess.m365ForwardingRule":
				from .networkaccess_m365_forwarding_rule import NetworkaccessM365ForwardingRule
				return NetworkaccessM365ForwardingRule.model_validate(data)
			if mapping_key == "#microsoft.graph.networkaccess.privateAccessForwardingRule":
				from .networkaccess_private_access_forwarding_rule import NetworkaccessPrivateAccessForwardingRule
				return NetworkaccessPrivateAccessForwardingRule.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e


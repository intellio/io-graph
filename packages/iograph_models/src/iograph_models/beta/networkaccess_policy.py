from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessPolicy(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	version: Optional[str] = Field(alias="version", default=None,)
	policyRules: Optional[list[Annotated[Union[NetworkaccessFilteringRule, NetworkaccessFqdnFilteringRule, NetworkaccessWebCategoryFilteringRule, NetworkaccessForwardingRule, NetworkaccessInternetAccessForwardingRule, NetworkaccessM365ForwardingRule, NetworkaccessPrivateAccessForwardingRule],Field(discriminator="odata_type")]]] = Field(alias="policyRules", default=None,)

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
			if mapping_key == "#microsoft.graph.networkaccess.filteringPolicy":
				from .networkaccess_filtering_policy import NetworkaccessFilteringPolicy
				return NetworkaccessFilteringPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.networkaccess.forwardingPolicy":
				from .networkaccess_forwarding_policy import NetworkaccessForwardingPolicy
				return NetworkaccessForwardingPolicy.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .networkaccess_filtering_rule import NetworkaccessFilteringRule
from .networkaccess_fqdn_filtering_rule import NetworkaccessFqdnFilteringRule
from .networkaccess_web_category_filtering_rule import NetworkaccessWebCategoryFilteringRule
from .networkaccess_forwarding_rule import NetworkaccessForwardingRule
from .networkaccess_internet_access_forwarding_rule import NetworkaccessInternetAccessForwardingRule
from .networkaccess_m365_forwarding_rule import NetworkaccessM365ForwardingRule
from .networkaccess_private_access_forwarding_rule import NetworkaccessPrivateAccessForwardingRule


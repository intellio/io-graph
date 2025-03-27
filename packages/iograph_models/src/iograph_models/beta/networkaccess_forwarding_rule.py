from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessForwardingRule(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.networkaccess.forwardingRule"] = Field(alias="@odata.type", default="#microsoft.graph.networkaccess.forwardingRule")
	name: Optional[str] = Field(alias="name", default=None,)
	action: Optional[NetworkaccessForwardingRuleAction | str] = Field(alias="action", default=None,)
	destinations: Optional[list[Annotated[Union[NetworkaccessFqdn, NetworkaccessIpAddress, NetworkaccessIpRange, NetworkaccessIpSubnet, NetworkaccessUrl, NetworkaccessWebCategory],Field(discriminator="odata_type")]]] = Field(alias="destinations", default=None,)
	ruleType: Optional[NetworkaccessNetworkDestinationType | str] = Field(alias="ruleType", default=None,)

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

from .networkaccess_forwarding_rule_action import NetworkaccessForwardingRuleAction
from .networkaccess_fqdn import NetworkaccessFqdn
from .networkaccess_ip_address import NetworkaccessIpAddress
from .networkaccess_ip_range import NetworkaccessIpRange
from .networkaccess_ip_subnet import NetworkaccessIpSubnet
from .networkaccess_url import NetworkaccessUrl
from .networkaccess_web_category import NetworkaccessWebCategory
from .networkaccess_network_destination_type import NetworkaccessNetworkDestinationType


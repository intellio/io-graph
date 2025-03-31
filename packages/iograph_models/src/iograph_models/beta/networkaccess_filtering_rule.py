from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class NetworkaccessFilteringRule(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.networkaccess.filteringRule"] = Field(alias="@odata.type", default="#microsoft.graph.networkaccess.filteringRule")
	name: Optional[str] = Field(alias="name", default=None,)
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
			if mapping_key == "#microsoft.graph.networkaccess.fqdnFilteringRule":
				from .networkaccess_fqdn_filtering_rule import NetworkaccessFqdnFilteringRule
				return NetworkaccessFqdnFilteringRule.model_validate(data)
			if mapping_key == "#microsoft.graph.networkaccess.webCategoryFilteringRule":
				from .networkaccess_web_category_filtering_rule import NetworkaccessWebCategoryFilteringRule
				return NetworkaccessWebCategoryFilteringRule.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .networkaccess_fqdn import NetworkaccessFqdn
from .networkaccess_ip_address import NetworkaccessIpAddress
from .networkaccess_ip_range import NetworkaccessIpRange
from .networkaccess_ip_subnet import NetworkaccessIpSubnet
from .networkaccess_url import NetworkaccessUrl
from .networkaccess_web_category import NetworkaccessWebCategory
from .networkaccess_network_destination_type import NetworkaccessNetworkDestinationType

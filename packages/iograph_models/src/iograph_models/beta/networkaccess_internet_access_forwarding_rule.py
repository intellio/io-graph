from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from pydantic import BaseModel, Field


class NetworkaccessInternetAccessForwardingRule(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.networkaccess.internetAccessForwardingRule"] = Field(alias="@odata.type", default="#microsoft.graph.networkaccess.internetAccessForwardingRule")
	name: Optional[str] = Field(alias="name", default=None,)
	action: Optional[NetworkaccessForwardingRuleAction | str] = Field(alias="action", default=None,)
	destinations: Optional[list[Annotated[Union[NetworkaccessFqdn, NetworkaccessIpAddress, NetworkaccessIpRange, NetworkaccessIpSubnet, NetworkaccessUrl, NetworkaccessWebCategory],Field(discriminator="odata_type")]]] = Field(alias="destinations", default=None,)
	ruleType: Optional[NetworkaccessNetworkDestinationType | str] = Field(alias="ruleType", default=None,)
	ports: Optional[list[str]] = Field(alias="ports", default=None,)
	protocol: Optional[NetworkaccessNetworkingProtocol | str] = Field(alias="protocol", default=None,)

from .networkaccess_forwarding_rule_action import NetworkaccessForwardingRuleAction
from .networkaccess_fqdn import NetworkaccessFqdn
from .networkaccess_ip_address import NetworkaccessIpAddress
from .networkaccess_ip_range import NetworkaccessIpRange
from .networkaccess_ip_subnet import NetworkaccessIpSubnet
from .networkaccess_url import NetworkaccessUrl
from .networkaccess_web_category import NetworkaccessWebCategory
from .networkaccess_network_destination_type import NetworkaccessNetworkDestinationType
from .networkaccess_networking_protocol import NetworkaccessNetworkingProtocol

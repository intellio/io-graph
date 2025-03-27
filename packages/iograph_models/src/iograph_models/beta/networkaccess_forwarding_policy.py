from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessForwardingPolicy(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.networkaccess.forwardingPolicy"] = Field(alias="@odata.type", default="#microsoft.graph.networkaccess.forwardingPolicy")
	description: Optional[str] = Field(alias="description", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	version: Optional[str] = Field(alias="version", default=None,)
	policyRules: Optional[list[Annotated[Union[NetworkaccessFilteringRule, NetworkaccessFqdnFilteringRule, NetworkaccessWebCategoryFilteringRule, NetworkaccessForwardingRule, NetworkaccessInternetAccessForwardingRule, NetworkaccessM365ForwardingRule, NetworkaccessPrivateAccessForwardingRule]],Field(discriminator="odata_type")]]] = Field(alias="policyRules", default=None,)
	trafficForwardingType: Optional[NetworkaccessTrafficForwardingType | str] = Field(alias="trafficForwardingType", default=None,)

from .networkaccess_filtering_rule import NetworkaccessFilteringRule
from .networkaccess_fqdn_filtering_rule import NetworkaccessFqdnFilteringRule
from .networkaccess_web_category_filtering_rule import NetworkaccessWebCategoryFilteringRule
from .networkaccess_forwarding_rule import NetworkaccessForwardingRule
from .networkaccess_internet_access_forwarding_rule import NetworkaccessInternetAccessForwardingRule
from .networkaccess_m365_forwarding_rule import NetworkaccessM365ForwardingRule
from .networkaccess_private_access_forwarding_rule import NetworkaccessPrivateAccessForwardingRule
from .networkaccess_traffic_forwarding_type import NetworkaccessTrafficForwardingType


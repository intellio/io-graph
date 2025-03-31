from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field


class NetworkaccessPolicyRuleCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[NetworkaccessFqdnFilteringRule, NetworkaccessWebCategoryFilteringRule, NetworkaccessInternetAccessForwardingRule, NetworkaccessM365ForwardingRule, NetworkaccessPrivateAccessForwardingRule],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .networkaccess_fqdn_filtering_rule import NetworkaccessFqdnFilteringRule
from .networkaccess_web_category_filtering_rule import NetworkaccessWebCategoryFilteringRule
from .networkaccess_internet_access_forwarding_rule import NetworkaccessInternetAccessForwardingRule
from .networkaccess_m365_forwarding_rule import NetworkaccessM365ForwardingRule
from .networkaccess_private_access_forwarding_rule import NetworkaccessPrivateAccessForwardingRule

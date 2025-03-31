from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field


class NetworkaccessRuleDestinationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[NetworkaccessFqdn, NetworkaccessIpAddress, NetworkaccessIpRange, NetworkaccessIpSubnet, NetworkaccessUrl, NetworkaccessWebCategory],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .networkaccess_fqdn import NetworkaccessFqdn
from .networkaccess_ip_address import NetworkaccessIpAddress
from .networkaccess_ip_range import NetworkaccessIpRange
from .networkaccess_ip_subnet import NetworkaccessIpSubnet
from .networkaccess_url import NetworkaccessUrl
from .networkaccess_web_category import NetworkaccessWebCategory

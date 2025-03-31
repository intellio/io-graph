from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field


class WindowsNetworkIsolationPolicy(BaseModel):
	enterpriseCloudResources: Optional[list[ProxiedDomain]] = Field(alias="enterpriseCloudResources", default=None,)
	enterpriseInternalProxyServers: Optional[list[str]] = Field(alias="enterpriseInternalProxyServers", default=None,)
	enterpriseIPRanges: Optional[list[Annotated[Union[IPv4CidrRange, IPv4Range, IPv6CidrRange, IPv6Range],Field(discriminator="odata_type")]]] = Field(alias="enterpriseIPRanges", default=None,)
	enterpriseIPRangesAreAuthoritative: Optional[bool] = Field(alias="enterpriseIPRangesAreAuthoritative", default=None,)
	enterpriseNetworkDomainNames: Optional[list[str]] = Field(alias="enterpriseNetworkDomainNames", default=None,)
	enterpriseProxyServers: Optional[list[str]] = Field(alias="enterpriseProxyServers", default=None,)
	enterpriseProxyServersAreAuthoritative: Optional[bool] = Field(alias="enterpriseProxyServersAreAuthoritative", default=None,)
	neutralDomainResources: Optional[list[str]] = Field(alias="neutralDomainResources", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .proxied_domain import ProxiedDomain
from .i_pv4_cidr_range import IPv4CidrRange
from .i_pv4_range import IPv4Range
from .i_pv6_cidr_range import IPv6CidrRange
from .i_pv6_range import IPv6Range

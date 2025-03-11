from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsNetworkIsolationPolicy(BaseModel):
	enterpriseCloudResources: Optional[list[ProxiedDomain]] = Field(alias="enterpriseCloudResources",default=None,)
	enterpriseInternalProxyServers: Optional[list[str]] = Field(alias="enterpriseInternalProxyServers",default=None,)
	enterpriseIPRanges: SerializeAsAny[Optional[list[IpRange]]] = Field(alias="enterpriseIPRanges",default=None,)
	enterpriseIPRangesAreAuthoritative: Optional[bool] = Field(alias="enterpriseIPRangesAreAuthoritative",default=None,)
	enterpriseNetworkDomainNames: Optional[list[str]] = Field(alias="enterpriseNetworkDomainNames",default=None,)
	enterpriseProxyServers: Optional[list[str]] = Field(alias="enterpriseProxyServers",default=None,)
	enterpriseProxyServersAreAuthoritative: Optional[bool] = Field(alias="enterpriseProxyServersAreAuthoritative",default=None,)
	neutralDomainResources: Optional[list[str]] = Field(alias="neutralDomainResources",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .proxied_domain import ProxiedDomain
from .ip_range import IpRange


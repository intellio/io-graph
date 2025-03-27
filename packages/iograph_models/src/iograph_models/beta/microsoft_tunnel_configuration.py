from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class MicrosoftTunnelConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	advancedSettings: Optional[list[KeyValuePair]] = Field(alias="advancedSettings", default=None,)
	defaultDomainSuffix: Optional[str] = Field(alias="defaultDomainSuffix", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	disableUdpConnections: Optional[bool] = Field(alias="disableUdpConnections", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	dnsServers: Optional[list[str]] = Field(alias="dnsServers", default=None,)
	ipv6Network: Optional[str] = Field(alias="ipv6Network", default=None,)
	lastUpdateDateTime: Optional[datetime] = Field(alias="lastUpdateDateTime", default=None,)
	listenPort: Optional[int] = Field(alias="listenPort", default=None,)
	network: Optional[str] = Field(alias="network", default=None,)
	roleScopeTagIds: Optional[list[str]] = Field(alias="roleScopeTagIds", default=None,)
	routeExcludes: Optional[list[str]] = Field(alias="routeExcludes", default=None,)
	routeIncludes: Optional[list[str]] = Field(alias="routeIncludes", default=None,)
	routesExclude: Optional[list[str]] = Field(alias="routesExclude", default=None,)
	routesInclude: Optional[list[str]] = Field(alias="routesInclude", default=None,)
	splitDNS: Optional[list[str]] = Field(alias="splitDNS", default=None,)

from .key_value_pair import KeyValuePair


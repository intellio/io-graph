from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityEndpointDiscoveredCloudAppDetail(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.security.endpointDiscoveredCloudAppDetail"] = Field(alias="@odata.type",)
	category: Optional[SecurityAppCategory | str] = Field(alias="category", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	domains: Optional[list[str]] = Field(alias="domains", default=None,)
	downloadNetworkTrafficInBytes: Optional[int] = Field(alias="downloadNetworkTrafficInBytes", default=None,)
	firstSeenDateTime: Optional[datetime] = Field(alias="firstSeenDateTime", default=None,)
	ipAddressCount: Optional[int] = Field(alias="ipAddressCount", default=None,)
	lastSeenDateTime: Optional[datetime] = Field(alias="lastSeenDateTime", default=None,)
	riskScore: Optional[int] = Field(alias="riskScore", default=None,)
	tags: Optional[list[str]] = Field(alias="tags", default=None,)
	transactionCount: Optional[int] = Field(alias="transactionCount", default=None,)
	uploadNetworkTrafficInBytes: Optional[int] = Field(alias="uploadNetworkTrafficInBytes", default=None,)
	userCount: Optional[int] = Field(alias="userCount", default=None,)
	appInfo: Optional[SecurityDiscoveredCloudAppInfo] = Field(alias="appInfo", default=None,)
	ipAddresses: Optional[list[SecurityDiscoveredCloudAppIPAddress]] = Field(alias="ipAddresses", default=None,)
	users: Optional[list[SecurityDiscoveredCloudAppUser]] = Field(alias="users", default=None,)
	deviceCount: Optional[int] = Field(alias="deviceCount", default=None,)
	devices: Optional[list[SecurityDiscoveredCloudAppDevice]] = Field(alias="devices", default=None,)

from .security_app_category import SecurityAppCategory
from .security_discovered_cloud_app_info import SecurityDiscoveredCloudAppInfo
from .security_discovered_cloud_app_i_p_address import SecurityDiscoveredCloudAppIPAddress
from .security_discovered_cloud_app_user import SecurityDiscoveredCloudAppUser
from .security_discovered_cloud_app_device import SecurityDiscoveredCloudAppDevice

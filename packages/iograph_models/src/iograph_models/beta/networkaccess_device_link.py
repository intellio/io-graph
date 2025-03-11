from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessDeviceLink(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	bandwidthCapacityInMbps: Optional[NetworkaccessBandwidthCapacityInMbps | str] = Field(alias="bandwidthCapacityInMbps",default=None,)
	bgpConfiguration: Optional[NetworkaccessBgpConfiguration] = Field(alias="bgpConfiguration",default=None,)
	deviceVendor: Optional[NetworkaccessDeviceVendor | str] = Field(alias="deviceVendor",default=None,)
	ipAddress: Optional[str] = Field(alias="ipAddress",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	name: Optional[str] = Field(alias="name",default=None,)
	redundancyConfiguration: Optional[NetworkaccessRedundancyConfiguration] = Field(alias="redundancyConfiguration",default=None,)
	tunnelConfiguration: SerializeAsAny[Optional[NetworkaccessTunnelConfiguration]] = Field(alias="tunnelConfiguration",default=None,)

from .networkaccess_bandwidth_capacity_in_mbps import NetworkaccessBandwidthCapacityInMbps
from .networkaccess_bgp_configuration import NetworkaccessBgpConfiguration
from .networkaccess_device_vendor import NetworkaccessDeviceVendor
from .networkaccess_redundancy_configuration import NetworkaccessRedundancyConfiguration
from .networkaccess_tunnel_configuration import NetworkaccessTunnelConfiguration


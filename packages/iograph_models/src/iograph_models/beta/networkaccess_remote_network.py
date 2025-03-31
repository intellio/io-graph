from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class NetworkaccessRemoteNetwork(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.networkaccess.remoteNetwork"] = Field(alias="@odata.type",)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	region: Optional[NetworkaccessRegion | str] = Field(alias="region", default=None,)
	version: Optional[str] = Field(alias="version", default=None,)
	connectivityConfiguration: Optional[NetworkaccessRemoteNetworkConnectivityConfiguration] = Field(alias="connectivityConfiguration", default=None,)
	deviceLinks: Optional[list[NetworkaccessDeviceLink]] = Field(alias="deviceLinks", default=None,)
	forwardingProfiles: Optional[list[NetworkaccessForwardingProfile]] = Field(alias="forwardingProfiles", default=None,)

from .networkaccess_region import NetworkaccessRegion
from .networkaccess_remote_network_connectivity_configuration import NetworkaccessRemoteNetworkConnectivityConfiguration
from .networkaccess_device_link import NetworkaccessDeviceLink
from .networkaccess_forwarding_profile import NetworkaccessForwardingProfile

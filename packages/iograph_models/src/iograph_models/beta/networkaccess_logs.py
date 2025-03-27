from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessLogs(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	remoteNetworks: Optional[list[NetworkaccessRemoteNetworkHealthEvent]] = Field(alias="remoteNetworks", default=None,)
	traffic: Optional[list[NetworkaccessNetworkAccessTraffic]] = Field(alias="traffic", default=None,)

from .networkaccess_remote_network_health_event import NetworkaccessRemoteNetworkHealthEvent
from .networkaccess_network_access_traffic import NetworkaccessNetworkAccessTraffic


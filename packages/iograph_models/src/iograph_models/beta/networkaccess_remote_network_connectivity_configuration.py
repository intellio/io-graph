from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class NetworkaccessRemoteNetworkConnectivityConfiguration(BaseModel):
	remoteNetworkId: Optional[str] = Field(alias="remoteNetworkId", default=None,)
	remoteNetworkName: Optional[str] = Field(alias="remoteNetworkName", default=None,)
	links: Optional[list[NetworkaccessConnectivityConfigurationLink]] = Field(alias="links", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .networkaccess_connectivity_configuration_link import NetworkaccessConnectivityConfigurationLink

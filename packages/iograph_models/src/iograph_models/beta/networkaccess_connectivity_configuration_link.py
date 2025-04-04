from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class NetworkaccessConnectivityConfigurationLink(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.networkaccess.connectivityConfigurationLink"] = Field(alias="@odata.type", default="#microsoft.graph.networkaccess.connectivityConfigurationLink")
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	localConfigurations: Optional[list[NetworkaccessLocalConnectivityConfiguration]] = Field(alias="localConfigurations", default=None,)
	peerConfiguration: Optional[NetworkaccessPeerConnectivityConfiguration] = Field(alias="peerConfiguration", default=None,)

from .networkaccess_local_connectivity_configuration import NetworkaccessLocalConnectivityConfiguration
from .networkaccess_peer_connectivity_configuration import NetworkaccessPeerConnectivityConfiguration

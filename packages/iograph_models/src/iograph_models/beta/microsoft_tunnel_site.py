from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class MicrosoftTunnelSite(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.microsoftTunnelSite"] = Field(alias="@odata.type", default="#microsoft.graph.microsoftTunnelSite")
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	internalNetworkProbeUrl: Optional[str] = Field(alias="internalNetworkProbeUrl", default=None,)
	publicAddress: Optional[str] = Field(alias="publicAddress", default=None,)
	roleScopeTagIds: Optional[list[str]] = Field(alias="roleScopeTagIds", default=None,)
	upgradeAutomatically: Optional[bool] = Field(alias="upgradeAutomatically", default=None,)
	upgradeAvailable: Optional[bool] = Field(alias="upgradeAvailable", default=None,)
	upgradeWindowEndTime: Optional[str] = Field(alias="upgradeWindowEndTime", default=None,)
	upgradeWindowStartTime: Optional[str] = Field(alias="upgradeWindowStartTime", default=None,)
	upgradeWindowUtcOffsetInMinutes: Optional[int] = Field(alias="upgradeWindowUtcOffsetInMinutes", default=None,)
	microsoftTunnelConfiguration: Optional[MicrosoftTunnelConfiguration] = Field(alias="microsoftTunnelConfiguration", default=None,)
	microsoftTunnelServers: Optional[list[MicrosoftTunnelServer]] = Field(alias="microsoftTunnelServers", default=None,)

from .microsoft_tunnel_configuration import MicrosoftTunnelConfiguration
from .microsoft_tunnel_server import MicrosoftTunnelServer

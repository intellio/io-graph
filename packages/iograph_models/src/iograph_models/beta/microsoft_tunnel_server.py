from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class MicrosoftTunnelServer(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	agentImageDigest: Optional[str] = Field(alias="agentImageDigest",default=None,)
	deploymentMode: Optional[MicrosoftTunnelDeploymentMode | str] = Field(alias="deploymentMode",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	lastCheckinDateTime: Optional[datetime] = Field(alias="lastCheckinDateTime",default=None,)
	serverImageDigest: Optional[str] = Field(alias="serverImageDigest",default=None,)
	tunnelServerHealthStatus: Optional[MicrosoftTunnelServerHealthStatus | str] = Field(alias="tunnelServerHealthStatus",default=None,)

from .microsoft_tunnel_deployment_mode import MicrosoftTunnelDeploymentMode
from .microsoft_tunnel_server_health_status import MicrosoftTunnelServerHealthStatus


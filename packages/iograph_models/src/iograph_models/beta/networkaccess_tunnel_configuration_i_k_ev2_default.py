from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessTunnelConfigurationIKEv2Default(BaseModel):
	preSharedKey: Optional[str] = Field(alias="preSharedKey", default=None,)
	zoneRedundancyPreSharedKey: Optional[str] = Field(alias="zoneRedundancyPreSharedKey", default=None,)
	odata_type: Literal["#microsoft.graph.networkaccess.tunnelConfigurationIKEv2Default"] = Field(alias="@odata.type", default="#microsoft.graph.networkaccess.tunnelConfigurationIKEv2Default")



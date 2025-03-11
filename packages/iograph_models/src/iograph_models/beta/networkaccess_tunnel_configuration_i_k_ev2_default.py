from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessTunnelConfigurationIKEv2Default(BaseModel):
	preSharedKey: Optional[str] = Field(alias="preSharedKey",default=None,)
	zoneRedundancyPreSharedKey: Optional[str] = Field(alias="zoneRedundancyPreSharedKey",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)



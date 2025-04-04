from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MicrosoftTunnelHealthThresholdCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[MicrosoftTunnelHealthThreshold]] = Field(alias="value", default=None,)

from .microsoft_tunnel_health_threshold import MicrosoftTunnelHealthThreshold

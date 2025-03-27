from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MicrosoftTunnelSiteCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[MicrosoftTunnelSite]] = Field(alias="value", default=None,)

from .microsoft_tunnel_site import MicrosoftTunnelSite


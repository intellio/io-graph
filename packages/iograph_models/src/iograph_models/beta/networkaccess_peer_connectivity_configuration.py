from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessPeerConnectivityConfiguration(BaseModel):
	asn: Optional[int] = Field(alias="asn", default=None,)
	bgpAddress: Optional[str] = Field(alias="bgpAddress", default=None,)
	endpoint: Optional[str] = Field(alias="endpoint", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)



from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessBgpConfiguration(BaseModel):
	asn: Optional[int] = Field(alias="asn",default=None,)
	ipAddress: Optional[str] = Field(alias="ipAddress",default=None,)
	localIpAddress: Optional[str] = Field(alias="localIpAddress",default=None,)
	peerIpAddress: Optional[str] = Field(alias="peerIpAddress",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)



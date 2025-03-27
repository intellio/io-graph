from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkInterface(BaseModel):
	description: Optional[str] = Field(alias="description", default=None,)
	ipV4Address: Optional[str] = Field(alias="ipV4Address", default=None,)
	ipV6Address: Optional[str] = Field(alias="ipV6Address", default=None,)
	localIpV6Address: Optional[str] = Field(alias="localIpV6Address", default=None,)
	macAddress: Optional[str] = Field(alias="macAddress", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)



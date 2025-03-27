from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class VpnDnsRule(BaseModel):
	autoTrigger: Optional[bool] = Field(alias="autoTrigger", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	persistent: Optional[bool] = Field(alias="persistent", default=None,)
	proxyServerUri: Optional[str] = Field(alias="proxyServerUri", default=None,)
	servers: Optional[list[str]] = Field(alias="servers", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)



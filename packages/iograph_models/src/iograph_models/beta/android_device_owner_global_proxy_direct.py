from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AndroidDeviceOwnerGlobalProxyDirect(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	excludedHosts: Optional[list[str]] = Field(alias="excludedHosts",default=None,)
	host: Optional[str] = Field(alias="host",default=None,)
	port: Optional[int] = Field(alias="port",default=None,)



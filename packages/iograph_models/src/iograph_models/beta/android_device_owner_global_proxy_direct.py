from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class AndroidDeviceOwnerGlobalProxyDirect(BaseModel):
	odata_type: Literal["#microsoft.graph.androidDeviceOwnerGlobalProxyDirect"] = Field(alias="@odata.type", default="#microsoft.graph.androidDeviceOwnerGlobalProxyDirect")
	excludedHosts: Optional[list[str]] = Field(alias="excludedHosts", default=None,)
	host: Optional[str] = Field(alias="host", default=None,)
	port: Optional[int] = Field(alias="port", default=None,)



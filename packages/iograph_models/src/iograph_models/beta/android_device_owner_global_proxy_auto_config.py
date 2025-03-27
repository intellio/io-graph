from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class AndroidDeviceOwnerGlobalProxyAutoConfig(BaseModel):
	odata_type: Literal["#microsoft.graph.androidDeviceOwnerGlobalProxyAutoConfig"] = Field(alias="@odata.type", default="#microsoft.graph.androidDeviceOwnerGlobalProxyAutoConfig")
	proxyAutoConfigURL: Optional[str] = Field(alias="proxyAutoConfigURL", default=None,)



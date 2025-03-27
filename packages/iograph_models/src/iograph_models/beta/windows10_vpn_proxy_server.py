from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class Windows10VpnProxyServer(BaseModel):
	address: Optional[str] = Field(alias="address", default=None,)
	automaticConfigurationScriptUrl: Optional[str] = Field(alias="automaticConfigurationScriptUrl", default=None,)
	port: Optional[int] = Field(alias="port", default=None,)
	odata_type: Literal["#microsoft.graph.windows10VpnProxyServer"] = Field(alias="@odata.type", default="#microsoft.graph.windows10VpnProxyServer")
	bypassProxyServerForLocalAddress: Optional[bool] = Field(alias="bypassProxyServerForLocalAddress", default=None,)



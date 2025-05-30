from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class Windows81VpnProxyServer(BaseModel):
	address: Optional[str] = Field(alias="address", default=None,)
	automaticConfigurationScriptUrl: Optional[str] = Field(alias="automaticConfigurationScriptUrl", default=None,)
	port: Optional[int] = Field(alias="port", default=None,)
	odata_type: Literal["#microsoft.graph.windows81VpnProxyServer"] = Field(alias="@odata.type", default="#microsoft.graph.windows81VpnProxyServer")
	automaticallyDetectProxySettings: Optional[bool] = Field(alias="automaticallyDetectProxySettings", default=None,)
	bypassProxyServerForLocalAddress: Optional[bool] = Field(alias="bypassProxyServerForLocalAddress", default=None,)


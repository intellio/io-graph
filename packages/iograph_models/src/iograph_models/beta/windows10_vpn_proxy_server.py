from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Windows10VpnProxyServer(BaseModel):
	address: Optional[str] = Field(alias="address",default=None,)
	automaticConfigurationScriptUrl: Optional[str] = Field(alias="automaticConfigurationScriptUrl",default=None,)
	port: Optional[int] = Field(alias="port",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	bypassProxyServerForLocalAddress: Optional[bool] = Field(alias="bypassProxyServerForLocalAddress",default=None,)



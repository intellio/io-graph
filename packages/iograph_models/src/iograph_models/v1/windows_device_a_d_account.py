from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsDeviceADAccount(BaseModel):
	password: Optional[str] = Field(alias="password", default=None,)
	odata_type: Literal["#microsoft.graph.windowsDeviceADAccount"] = Field(alias="@odata.type", default="#microsoft.graph.windowsDeviceADAccount")
	domainName: Optional[str] = Field(alias="domainName", default=None,)
	userName: Optional[str] = Field(alias="userName", default=None,)



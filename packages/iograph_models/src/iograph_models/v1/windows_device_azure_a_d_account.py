from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class WindowsDeviceAzureADAccount(BaseModel):
	password: Optional[str] = Field(alias="password", default=None,)
	odata_type: Literal["#microsoft.graph.windowsDeviceAzureADAccount"] = Field(alias="@odata.type", default="#microsoft.graph.windowsDeviceAzureADAccount")
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName", default=None,)


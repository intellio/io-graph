from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Windows10NetworkProxyServer(BaseModel):
	address: Optional[str] = Field(default=None,alias="address",)
	exceptions: list[Optional[str]] = Field(alias="exceptions",)
	useForLocalAddresses: Optional[bool] = Field(default=None,alias="useForLocalAddresses",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)



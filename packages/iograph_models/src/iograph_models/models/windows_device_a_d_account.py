from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WindowsDeviceADAccount(BaseModel):
	password: Optional[str] = Field(default=None,alias="password",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	domainName: Optional[str] = Field(default=None,alias="domainName",)
	userName: Optional[str] = Field(default=None,alias="userName",)



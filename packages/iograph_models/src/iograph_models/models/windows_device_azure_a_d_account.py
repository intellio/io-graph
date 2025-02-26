from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WindowsDeviceAzureADAccount(BaseModel):
	password: Optional[str] = Field(default=None,alias="password",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	userPrincipalName: Optional[str] = Field(default=None,alias="userPrincipalName",)



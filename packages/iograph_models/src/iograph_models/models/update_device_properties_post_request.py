from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Update_device_propertiesPostRequest(BaseModel):
	userPrincipalName: Optional[str] = Field(default=None,alias="userPrincipalName",)
	addressableUserName: Optional[str] = Field(default=None,alias="addressableUserName",)
	groupTag: Optional[str] = Field(default=None,alias="groupTag",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)



from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Update_device_propertiesPostRequest(BaseModel):
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName", default=None,)
	addressableUserName: Optional[str] = Field(alias="addressableUserName", default=None,)
	groupTag: Optional[str] = Field(alias="groupTag", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)


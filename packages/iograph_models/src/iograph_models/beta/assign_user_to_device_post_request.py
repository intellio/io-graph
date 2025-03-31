from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Assign_user_to_devicePostRequest(BaseModel):
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName", default=None,)
	addressableUserName: Optional[str] = Field(alias="addressableUserName", default=None,)


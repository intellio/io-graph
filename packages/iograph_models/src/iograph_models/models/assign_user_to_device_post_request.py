from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Assign_user_to_devicePostRequest(BaseModel):
	userPrincipalName: Optional[str] = Field(default=None,alias="userPrincipalName",)
	addressableUserName: Optional[str] = Field(default=None,alias="addressableUserName",)



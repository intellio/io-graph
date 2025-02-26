from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Delete_user_from_shared_apple_devicePostRequest(BaseModel):
	userPrincipalName: Optional[str] = Field(default=None,alias="userPrincipalName",)



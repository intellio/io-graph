from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Change_passwordPostRequest(BaseModel):
	currentPassword: Optional[str] = Field(default=None,alias="currentPassword",)
	newPassword: Optional[str] = Field(default=None,alias="newPassword",)



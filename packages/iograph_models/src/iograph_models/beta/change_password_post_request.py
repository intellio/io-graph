from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Change_passwordPostRequest(BaseModel):
	currentPassword: Optional[str] = Field(alias="currentPassword", default=None,)
	newPassword: Optional[str] = Field(alias="newPassword", default=None,)



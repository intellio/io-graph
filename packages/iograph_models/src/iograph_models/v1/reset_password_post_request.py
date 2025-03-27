from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Reset_passwordPostRequest(BaseModel):
	newPassword: Optional[str] = Field(alias="newPassword", default=None,)



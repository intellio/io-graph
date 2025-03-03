from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Set_user_preferred_presencePostRequest(BaseModel):
	availability: Optional[str] = Field(default=None,alias="availability",)
	activity: Optional[str] = Field(default=None,alias="activity",)
	expirationDuration: Optional[str] = Field(default=None,alias="expirationDuration",)



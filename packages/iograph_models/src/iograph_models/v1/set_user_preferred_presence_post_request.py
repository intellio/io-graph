from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Set_user_preferred_presencePostRequest(BaseModel):
	availability: Optional[str] = Field(alias="availability", default=None,)
	activity: Optional[str] = Field(alias="activity", default=None,)
	expirationDuration: Optional[str] = Field(alias="expirationDuration", default=None,)


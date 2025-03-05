from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Set_presencePostRequest(BaseModel):
	sessionId: Optional[str] = Field(default=None,alias="sessionId",)
	availability: Optional[str] = Field(default=None,alias="availability",)
	activity: Optional[str] = Field(default=None,alias="activity",)
	expirationDuration: Optional[str] = Field(default=None,alias="expirationDuration",)



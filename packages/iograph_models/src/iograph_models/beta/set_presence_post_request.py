from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Set_presencePostRequest(BaseModel):
	sessionId: Optional[str] = Field(alias="sessionId",default=None,)
	availability: Optional[str] = Field(alias="availability",default=None,)
	activity: Optional[str] = Field(alias="activity",default=None,)
	expirationDuration: Optional[str] = Field(alias="expirationDuration",default=None,)



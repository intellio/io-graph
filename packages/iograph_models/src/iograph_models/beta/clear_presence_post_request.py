from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Clear_presencePostRequest(BaseModel):
	sessionId: Optional[str] = Field(alias="sessionId", default=None,)


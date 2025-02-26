from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TokenMeetingInfo(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	token: Optional[str] = Field(default=None,alias="token",)



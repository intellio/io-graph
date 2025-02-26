from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class InviteNewBotResponse(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	inviteUri: Optional[str] = Field(default=None,alias="inviteUri",)



from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SkypeUserConversationMember(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	roles: list[Optional[str]] = Field(alias="roles",)
	visibleHistoryStartDateTime: Optional[datetime] = Field(default=None,alias="visibleHistoryStartDateTime",)
	skypeId: Optional[str] = Field(default=None,alias="skypeId",)



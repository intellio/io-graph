from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ChatMembersNotificationRecipient(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	chatId: Optional[str] = Field(default=None,alias="chatId",)



from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ChatMembersNotificationRecipient(BaseModel):
	odata_type: Literal["#microsoft.graph.chatMembersNotificationRecipient"] = Field(alias="@odata.type", default="#microsoft.graph.chatMembersNotificationRecipient")
	chatId: Optional[str] = Field(alias="chatId", default=None,)


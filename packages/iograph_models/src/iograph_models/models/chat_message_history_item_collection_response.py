from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ChatMessageHistoryItemCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[ChatMessageHistoryItem] = Field(alias="value",)

from .chat_message_history_item import ChatMessageHistoryItem


from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PinnedChatMessageInfo(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	message: Optional[ChatMessage] = Field(default=None,alias="message",)

from .chat_message import ChatMessage


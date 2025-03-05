from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PinnedChatMessageInfo(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	message: Optional[ChatMessage] = Field(alias="message",default=None,)

from .chat_message import ChatMessage


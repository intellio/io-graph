from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class PinnedChatMessageInfo(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.pinnedChatMessageInfo"] = Field(alias="@odata.type",)
	message: Optional[ChatMessage] = Field(alias="message", default=None,)

from .chat_message import ChatMessage

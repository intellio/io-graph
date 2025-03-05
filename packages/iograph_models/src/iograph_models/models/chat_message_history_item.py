from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ChatMessageHistoryItem(BaseModel):
	actions: Optional[ChatMessageActions] = Field(default=None,alias="actions",)
	modifiedDateTime: Optional[datetime] = Field(default=None,alias="modifiedDateTime",)
	reaction: Optional[ChatMessageReaction] = Field(default=None,alias="reaction",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .chat_message_actions import ChatMessageActions
from .chat_message_reaction import ChatMessageReaction


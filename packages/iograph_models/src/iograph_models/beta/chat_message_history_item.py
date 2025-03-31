from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class ChatMessageHistoryItem(BaseModel):
	actions: Optional[ChatMessageActions | str] = Field(alias="actions", default=None,)
	modifiedDateTime: Optional[datetime] = Field(alias="modifiedDateTime", default=None,)
	reaction: Optional[ChatMessageReaction] = Field(alias="reaction", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .chat_message_actions import ChatMessageActions
from .chat_message_reaction import ChatMessageReaction

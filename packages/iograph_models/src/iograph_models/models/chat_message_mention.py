from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ChatMessageMention(BaseModel):
	id: Optional[int] = Field(default=None,alias="id",)
	mentioned: Optional[ChatMessageMentionedIdentitySet] = Field(default=None,alias="mentioned",)
	mentionText: Optional[str] = Field(default=None,alias="mentionText",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet


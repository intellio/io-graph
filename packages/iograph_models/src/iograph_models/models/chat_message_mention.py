from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ChatMessageMention(BaseModel):
	id: Optional[int] = Field(alias="id",default=None,)
	mentioned: Optional[ChatMessageMentionedIdentitySet] = Field(alias="mentioned",default=None,)
	mentionText: Optional[str] = Field(alias="mentionText",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet


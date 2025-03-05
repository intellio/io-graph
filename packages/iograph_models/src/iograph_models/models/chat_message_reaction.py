from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ChatMessageReaction(BaseModel):
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	reactionContentUrl: Optional[str] = Field(default=None,alias="reactionContentUrl",)
	reactionType: Optional[str] = Field(default=None,alias="reactionType",)
	user: Optional[ChatMessageReactionIdentitySet] = Field(default=None,alias="user",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet


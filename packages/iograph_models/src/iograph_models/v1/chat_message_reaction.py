from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ChatMessageReaction(BaseModel):
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	reactionContentUrl: Optional[str] = Field(alias="reactionContentUrl", default=None,)
	reactionType: Optional[str] = Field(alias="reactionType", default=None,)
	user: Optional[ChatMessageReactionIdentitySet] = Field(alias="user", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet


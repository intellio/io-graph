from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ChatMessageMentionedIdentitySet(BaseModel):
	application: SerializeAsAny[Optional[Identity]] = Field(default=None,alias="application",)
	device: SerializeAsAny[Optional[Identity]] = Field(default=None,alias="device",)
	user: SerializeAsAny[Optional[Identity]] = Field(default=None,alias="user",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	conversation: Optional[TeamworkConversationIdentity] = Field(default=None,alias="conversation",)

from .identity import Identity
from .identity import Identity
from .identity import Identity
from .teamwork_conversation_identity import TeamworkConversationIdentity


from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ChatMessageMentionedIdentitySet(BaseModel):
	application: SerializeAsAny[Optional[Identity]] = Field(alias="application",default=None,)
	device: SerializeAsAny[Optional[Identity]] = Field(alias="device",default=None,)
	user: SerializeAsAny[Optional[Identity]] = Field(alias="user",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	conversation: Optional[TeamworkConversationIdentity] = Field(alias="conversation",default=None,)

from .identity import Identity
from .identity import Identity
from .identity import Identity
from .teamwork_conversation_identity import TeamworkConversationIdentity


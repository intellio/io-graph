from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import BaseModel, Field


class ChatRenamedEventMessageDetail(BaseModel):
	odata_type: Literal["#microsoft.graph.chatRenamedEventMessageDetail"] = Field(alias="@odata.type", default="#microsoft.graph.chatRenamedEventMessageDetail")
	chatDisplayName: Optional[str] = Field(alias="chatDisplayName", default=None,)
	chatId: Optional[str] = Field(alias="chatId", default=None,)
	initiator: Optional[Union[ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="initiator", default=None,discriminator="odata_type", )

from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet

from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class MessageUnpinnedEventMessageDetail(BaseModel):
	odata_type: Literal["#microsoft.graph.messageUnpinnedEventMessageDetail"] = Field(alias="@odata.type", default="#microsoft.graph.messageUnpinnedEventMessageDetail")
	eventDateTime: Optional[datetime] = Field(alias="eventDateTime", default=None,)
	initiator: Optional[Union[ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="initiator", default=None,discriminator="odata_type", )

from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet

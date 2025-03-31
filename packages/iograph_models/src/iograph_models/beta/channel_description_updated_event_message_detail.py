from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import BaseModel, Field


class ChannelDescriptionUpdatedEventMessageDetail(BaseModel):
	odata_type: Literal["#microsoft.graph.channelDescriptionUpdatedEventMessageDetail"] = Field(alias="@odata.type", default="#microsoft.graph.channelDescriptionUpdatedEventMessageDetail")
	channelDescription: Optional[str] = Field(alias="channelDescription", default=None,)
	channelId: Optional[str] = Field(alias="channelId", default=None,)
	initiator: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="initiator", default=None,discriminator="odata_type", )

from .ai_interaction_mentioned_identity_set import AiInteractionMentionedIdentitySet
from .approval_identity_set import ApprovalIdentitySet
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet

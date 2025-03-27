from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class ChannelSharingUpdatedEventMessageDetail(BaseModel):
	odata_type: Literal["#microsoft.graph.channelSharingUpdatedEventMessageDetail"] = Field(alias="@odata.type", default="#microsoft.graph.channelSharingUpdatedEventMessageDetail")
	initiator: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="initiator", default=None,discriminator="odata_type", )
	ownerTeamId: Optional[str] = Field(alias="ownerTeamId", default=None,)
	ownerTenantId: Optional[str] = Field(alias="ownerTenantId", default=None,)
	sharedChannelId: Optional[str] = Field(alias="sharedChannelId", default=None,)

from .ai_interaction_mentioned_identity_set import AiInteractionMentionedIdentitySet
from .approval_identity_set import ApprovalIdentitySet
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet


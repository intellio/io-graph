from __future__ import annotations
from typing import Optional
from typing import Union
from pydantic import BaseModel, Field


class IncomingContext(BaseModel):
	observedParticipantId: Optional[str] = Field(alias="observedParticipantId", default=None,)
	onBehalfOf: Optional[Union[ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="onBehalfOf", default=None,discriminator="odata_type", )
	sourceParticipantId: Optional[str] = Field(alias="sourceParticipantId", default=None,)
	transferor: Optional[Union[ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="transferor", default=None,discriminator="odata_type", )
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet

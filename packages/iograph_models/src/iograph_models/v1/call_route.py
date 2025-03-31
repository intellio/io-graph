from __future__ import annotations
from typing import Optional
from typing import Union
from pydantic import BaseModel, Field


class CallRoute(BaseModel):
	final: Optional[Union[ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="final", default=None,discriminator="odata_type", )
	original: Optional[Union[ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="original", default=None,discriminator="odata_type", )
	routingType: Optional[RoutingType | str] = Field(alias="routingType", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .routing_type import RoutingType

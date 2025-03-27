from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class TeamRenamedEventMessageDetail(BaseModel):
	odata_type: Literal["#microsoft.graph.teamRenamedEventMessageDetail"] = Field(alias="@odata.type", default="#microsoft.graph.teamRenamedEventMessageDetail")
	initiator: Optional[Union[ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="initiator", default=None,discriminator="odata_type", )
	teamDisplayName: Optional[str] = Field(alias="teamDisplayName", default=None,)
	teamId: Optional[str] = Field(alias="teamId", default=None,)

from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet


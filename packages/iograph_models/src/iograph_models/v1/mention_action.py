from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class MentionAction(BaseModel):
	mentionees: Optional[list[Annotated[Union[ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet],Field(discriminator="odata_type")]]] = Field(alias="mentionees", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet


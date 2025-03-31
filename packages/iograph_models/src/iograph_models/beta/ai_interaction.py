from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class AiInteraction(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.aiInteraction"] = Field(alias="@odata.type",)
	appClass: Optional[str] = Field(alias="appClass", default=None,)
	attachments: Optional[list[AiInteractionAttachment]] = Field(alias="attachments", default=None,)
	body: Optional[ItemBody] = Field(alias="body", default=None,)
	contexts: Optional[list[AiInteractionContext]] = Field(alias="contexts", default=None,)
	conversationType: Optional[str] = Field(alias="conversationType", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	etag: Optional[str] = Field(alias="etag", default=None,)
	from_: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="from", default=None,discriminator="odata_type", )
	interactionType: Optional[AiInteractionType | str] = Field(alias="interactionType", default=None,)
	links: Optional[list[AiInteractionLink]] = Field(alias="links", default=None,)
	locale: Optional[str] = Field(alias="locale", default=None,)
	mentions: Optional[list[AiInteractionMention]] = Field(alias="mentions", default=None,)
	requestId: Optional[str] = Field(alias="requestId", default=None,)
	sessionId: Optional[str] = Field(alias="sessionId", default=None,)

from .ai_interaction_attachment import AiInteractionAttachment
from .item_body import ItemBody
from .ai_interaction_context import AiInteractionContext
from .ai_interaction_mentioned_identity_set import AiInteractionMentionedIdentitySet
from .approval_identity_set import ApprovalIdentitySet
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .ai_interaction_type import AiInteractionType
from .ai_interaction_link import AiInteractionLink
from .ai_interaction_mention import AiInteractionMention

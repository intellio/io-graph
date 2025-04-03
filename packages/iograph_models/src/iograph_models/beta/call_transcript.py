from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class CallTranscript(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.callTranscript"] = Field(alias="@odata.type", default="#microsoft.graph.callTranscript")
	callId: Optional[str] = Field(alias="callId", default=None,)
	content: Optional[str] = Field(alias="content", default=None,)
	contentCorrelationId: Optional[str] = Field(alias="contentCorrelationId", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	endDateTime: Optional[datetime] = Field(alias="endDateTime", default=None,)
	meetingId: Optional[str] = Field(alias="meetingId", default=None,)
	meetingOrganizer: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="meetingOrganizer", default=None,discriminator="odata_type", )
	metadataContent: Optional[str] = Field(alias="metadataContent", default=None,)
	transcriptContentUrl: Optional[str] = Field(alias="transcriptContentUrl", default=None,)

from .ai_interaction_mentioned_identity_set import AiInteractionMentionedIdentitySet
from .approval_identity_set import ApprovalIdentitySet
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet

from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import BaseModel, Field


class CallTranscriptEventMessageDetail(BaseModel):
	odata_type: Literal["#microsoft.graph.callTranscriptEventMessageDetail"] = Field(alias="@odata.type", default="#microsoft.graph.callTranscriptEventMessageDetail")
	callId: Optional[str] = Field(alias="callId", default=None,)
	callTranscriptICalUid: Optional[str] = Field(alias="callTranscriptICalUid", default=None,)
	meetingOrganizer: Optional[Union[ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="meetingOrganizer", default=None,discriminator="odata_type", )

from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet

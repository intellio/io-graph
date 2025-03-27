from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class CallEndedEventMessageDetail(BaseModel):
	odata_type: Literal["#microsoft.graph.callEndedEventMessageDetail"] = Field(alias="@odata.type", default="#microsoft.graph.callEndedEventMessageDetail")
	callDuration: Optional[str] = Field(alias="callDuration", default=None,)
	callEventType: Optional[TeamworkCallEventType | str] = Field(alias="callEventType", default=None,)
	callId: Optional[str] = Field(alias="callId", default=None,)
	callParticipants: Optional[list[CallParticipantInfo]] = Field(alias="callParticipants", default=None,)
	initiator: Optional[Union[ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="initiator", default=None,discriminator="odata_type", )

from .teamwork_call_event_type import TeamworkCallEventType
from .call_participant_info import CallParticipantInfo
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet


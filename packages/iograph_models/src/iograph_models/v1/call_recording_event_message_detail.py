from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class CallRecordingEventMessageDetail(BaseModel):
	odata_type: Literal["#microsoft.graph.callRecordingEventMessageDetail"] = Field(alias="@odata.type", default="#microsoft.graph.callRecordingEventMessageDetail")
	callId: Optional[str] = Field(alias="callId", default=None,)
	callRecordingDisplayName: Optional[str] = Field(alias="callRecordingDisplayName", default=None,)
	callRecordingDuration: Optional[str] = Field(alias="callRecordingDuration", default=None,)
	callRecordingStatus: Optional[CallRecordingStatus | str] = Field(alias="callRecordingStatus", default=None,)
	callRecordingUrl: Optional[str] = Field(alias="callRecordingUrl", default=None,)
	initiator: Optional[Union[ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="initiator", default=None,discriminator="odata_type", )
	meetingOrganizer: Optional[Union[ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="meetingOrganizer", default=None,discriminator="odata_type", )

from .call_recording_status import CallRecordingStatus
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet


from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field


class CallRecordsCallRecord(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.callRecords.callRecord"] = Field(alias="@odata.type",)
	endDateTime: Optional[datetime] = Field(alias="endDateTime", default=None,)
	joinWebUrl: Optional[str] = Field(alias="joinWebUrl", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	modalities: Optional[list[CallRecordsModality | str]] = Field(alias="modalities", default=None,)
	organizer: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="organizer", default=None,discriminator="odata_type", )
	participants: Optional[list[Annotated[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet],Field(discriminator="odata_type")]]] = Field(alias="participants", default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime", default=None,)
	type: Optional[CallRecordsCallType | str] = Field(alias="type", default=None,)
	version: Optional[int] = Field(alias="version", default=None,)
	organizer_v2: Optional[CallRecordsOrganizer] = Field(alias="organizer_v2", default=None,)
	participants_v2: Optional[list[CallRecordsParticipant]] = Field(alias="participants_v2", default=None,)
	sessions: Optional[list[CallRecordsSession]] = Field(alias="sessions", default=None,)

from .call_records_modality import CallRecordsModality
from .ai_interaction_mentioned_identity_set import AiInteractionMentionedIdentitySet
from .approval_identity_set import ApprovalIdentitySet
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .call_records_call_type import CallRecordsCallType
from .call_records_organizer import CallRecordsOrganizer
from .call_records_participant import CallRecordsParticipant
from .call_records_session import CallRecordsSession

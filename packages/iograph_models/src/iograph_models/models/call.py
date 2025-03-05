from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Call(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	callbackUri: Optional[str] = Field(alias="callbackUri",default=None,)
	callChainId: Optional[str] = Field(alias="callChainId",default=None,)
	callOptions: SerializeAsAny[Optional[CallOptions]] = Field(alias="callOptions",default=None,)
	callRoutes: Optional[list[CallRoute]] = Field(alias="callRoutes",default=None,)
	chatInfo: Optional[ChatInfo] = Field(alias="chatInfo",default=None,)
	direction: Optional[str | CallDirection] = Field(alias="direction",default=None,)
	incomingContext: Optional[IncomingContext] = Field(alias="incomingContext",default=None,)
	mediaConfig: SerializeAsAny[Optional[MediaConfig]] = Field(alias="mediaConfig",default=None,)
	mediaState: Optional[CallMediaState] = Field(alias="mediaState",default=None,)
	meetingInfo: SerializeAsAny[Optional[MeetingInfo]] = Field(alias="meetingInfo",default=None,)
	myParticipantId: Optional[str] = Field(alias="myParticipantId",default=None,)
	requestedModalities: Optional[str | Modality] = Field(alias="requestedModalities",default=None,)
	resultInfo: Optional[ResultInfo] = Field(alias="resultInfo",default=None,)
	source: Optional[ParticipantInfo] = Field(alias="source",default=None,)
	state: Optional[str | CallState] = Field(alias="state",default=None,)
	subject: Optional[str] = Field(alias="subject",default=None,)
	targets: Optional[list[InvitationParticipantInfo]] = Field(alias="targets",default=None,)
	tenantId: Optional[str] = Field(alias="tenantId",default=None,)
	toneInfo: Optional[ToneInfo] = Field(alias="toneInfo",default=None,)
	transcription: Optional[CallTranscriptionInfo] = Field(alias="transcription",default=None,)
	audioRoutingGroups: Optional[list[AudioRoutingGroup]] = Field(alias="audioRoutingGroups",default=None,)
	contentSharingSessions: Optional[list[ContentSharingSession]] = Field(alias="contentSharingSessions",default=None,)
	operations: SerializeAsAny[Optional[list[CommsOperation]]] = Field(alias="operations",default=None,)
	participants: Optional[list[Participant]] = Field(alias="participants",default=None,)

from .call_options import CallOptions
from .call_route import CallRoute
from .chat_info import ChatInfo
from .call_direction import CallDirection
from .incoming_context import IncomingContext
from .media_config import MediaConfig
from .call_media_state import CallMediaState
from .meeting_info import MeetingInfo
from .modality import Modality
from .result_info import ResultInfo
from .participant_info import ParticipantInfo
from .call_state import CallState
from .invitation_participant_info import InvitationParticipantInfo
from .tone_info import ToneInfo
from .call_transcription_info import CallTranscriptionInfo
from .audio_routing_group import AudioRoutingGroup
from .content_sharing_session import ContentSharingSession
from .comms_operation import CommsOperation
from .participant import Participant


from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Call(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	callbackUri: Optional[str] = Field(default=None,alias="callbackUri",)
	callChainId: Optional[str] = Field(default=None,alias="callChainId",)
	callOptions: Optional[CallOptions] = Field(default=None,alias="callOptions",)
	callRoutes: list[CallRoute] = Field(alias="callRoutes",)
	chatInfo: Optional[ChatInfo] = Field(default=None,alias="chatInfo",)
	direction: Optional[CallDirection] = Field(default=None,alias="direction",)
	incomingContext: Optional[IncomingContext] = Field(default=None,alias="incomingContext",)
	mediaConfig: Optional[MediaConfig] = Field(default=None,alias="mediaConfig",)
	mediaState: Optional[CallMediaState] = Field(default=None,alias="mediaState",)
	meetingInfo: Optional[MeetingInfo] = Field(default=None,alias="meetingInfo",)
	myParticipantId: Optional[str] = Field(default=None,alias="myParticipantId",)
	requestedModalities: Optional[Modality] = Field(default=None,alias="requestedModalities",)
	resultInfo: Optional[ResultInfo] = Field(default=None,alias="resultInfo",)
	source: Optional[ParticipantInfo] = Field(default=None,alias="source",)
	state: Optional[CallState] = Field(default=None,alias="state",)
	subject: Optional[str] = Field(default=None,alias="subject",)
	targets: list[InvitationParticipantInfo] = Field(alias="targets",)
	tenantId: Optional[str] = Field(default=None,alias="tenantId",)
	toneInfo: Optional[ToneInfo] = Field(default=None,alias="toneInfo",)
	transcription: Optional[CallTranscriptionInfo] = Field(default=None,alias="transcription",)
	audioRoutingGroups: list[AudioRoutingGroup] = Field(alias="audioRoutingGroups",)
	contentSharingSessions: list[ContentSharingSession] = Field(alias="contentSharingSessions",)
	operations: list[CommsOperation] = Field(alias="operations",)
	participants: list[Participant] = Field(alias="participants",)

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


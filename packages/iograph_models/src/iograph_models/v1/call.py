from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from pydantic import BaseModel, Field


class Call(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.call"] = Field(alias="@odata.type",)
	callbackUri: Optional[str] = Field(alias="callbackUri", default=None,)
	callChainId: Optional[str] = Field(alias="callChainId", default=None,)
	callOptions: Optional[Union[IncomingCallOptions, OutgoingCallOptions]] = Field(alias="callOptions", default=None,discriminator="odata_type", )
	callRoutes: Optional[list[CallRoute]] = Field(alias="callRoutes", default=None,)
	chatInfo: Optional[ChatInfo] = Field(alias="chatInfo", default=None,)
	direction: Optional[CallDirection | str] = Field(alias="direction", default=None,)
	incomingContext: Optional[IncomingContext] = Field(alias="incomingContext", default=None,)
	mediaConfig: Optional[Union[AppHostedMediaConfig, ServiceHostedMediaConfig]] = Field(alias="mediaConfig", default=None,discriminator="odata_type", )
	mediaState: Optional[CallMediaState] = Field(alias="mediaState", default=None,)
	meetingInfo: Optional[Union[JoinMeetingIdMeetingInfo, OrganizerMeetingInfo, TokenMeetingInfo]] = Field(alias="meetingInfo", default=None,discriminator="odata_type", )
	myParticipantId: Optional[str] = Field(alias="myParticipantId", default=None,)
	requestedModalities: Optional[list[Modality | str]] = Field(alias="requestedModalities", default=None,)
	resultInfo: Optional[ResultInfo] = Field(alias="resultInfo", default=None,)
	source: Optional[ParticipantInfo] = Field(alias="source", default=None,)
	state: Optional[CallState | str] = Field(alias="state", default=None,)
	subject: Optional[str] = Field(alias="subject", default=None,)
	targets: Optional[list[InvitationParticipantInfo]] = Field(alias="targets", default=None,)
	tenantId: Optional[str] = Field(alias="tenantId", default=None,)
	toneInfo: Optional[ToneInfo] = Field(alias="toneInfo", default=None,)
	transcription: Optional[CallTranscriptionInfo] = Field(alias="transcription", default=None,)
	audioRoutingGroups: Optional[list[AudioRoutingGroup]] = Field(alias="audioRoutingGroups", default=None,)
	contentSharingSessions: Optional[list[ContentSharingSession]] = Field(alias="contentSharingSessions", default=None,)
	operations: Optional[list[Annotated[Union[AddLargeGalleryViewOperation, CancelMediaProcessingOperation, InviteParticipantsOperation, MuteParticipantOperation, PlayPromptOperation, RecordOperation, SendDtmfTonesOperation, StartHoldMusicOperation, StopHoldMusicOperation, SubscribeToToneOperation, UnmuteParticipantOperation, UpdateRecordingStatusOperation],Field(discriminator="odata_type")]]] = Field(alias="operations", default=None,)
	participants: Optional[list[Participant]] = Field(alias="participants", default=None,)

from .incoming_call_options import IncomingCallOptions
from .outgoing_call_options import OutgoingCallOptions
from .call_route import CallRoute
from .chat_info import ChatInfo
from .call_direction import CallDirection
from .incoming_context import IncomingContext
from .app_hosted_media_config import AppHostedMediaConfig
from .service_hosted_media_config import ServiceHostedMediaConfig
from .call_media_state import CallMediaState
from .join_meeting_id_meeting_info import JoinMeetingIdMeetingInfo
from .organizer_meeting_info import OrganizerMeetingInfo
from .token_meeting_info import TokenMeetingInfo
from .modality import Modality
from .result_info import ResultInfo
from .participant_info import ParticipantInfo
from .call_state import CallState
from .invitation_participant_info import InvitationParticipantInfo
from .tone_info import ToneInfo
from .call_transcription_info import CallTranscriptionInfo
from .audio_routing_group import AudioRoutingGroup
from .content_sharing_session import ContentSharingSession
from .add_large_gallery_view_operation import AddLargeGalleryViewOperation
from .cancel_media_processing_operation import CancelMediaProcessingOperation
from .invite_participants_operation import InviteParticipantsOperation
from .mute_participant_operation import MuteParticipantOperation
from .play_prompt_operation import PlayPromptOperation
from .record_operation import RecordOperation
from .send_dtmf_tones_operation import SendDtmfTonesOperation
from .start_hold_music_operation import StartHoldMusicOperation
from .stop_hold_music_operation import StopHoldMusicOperation
from .subscribe_to_tone_operation import SubscribeToToneOperation
from .unmute_participant_operation import UnmuteParticipantOperation
from .update_recording_status_operation import UpdateRecordingStatusOperation
from .participant import Participant

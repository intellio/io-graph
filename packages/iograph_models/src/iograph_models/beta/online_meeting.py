from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class OnlineMeeting(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.onlineMeeting"] = Field(alias="@odata.type", default="#microsoft.graph.onlineMeeting")
	allowAttendeeToEnableCamera: Optional[bool] = Field(alias="allowAttendeeToEnableCamera", default=None,)
	allowAttendeeToEnableMic: Optional[bool] = Field(alias="allowAttendeeToEnableMic", default=None,)
	allowBreakoutRooms: Optional[bool] = Field(alias="allowBreakoutRooms", default=None,)
	allowedLobbyAdmitters: Optional[AllowedLobbyAdmitterRoles | str] = Field(alias="allowedLobbyAdmitters", default=None,)
	allowedPresenters: Optional[OnlineMeetingPresenters | str] = Field(alias="allowedPresenters", default=None,)
	allowLiveShare: Optional[MeetingLiveShareOptions | str] = Field(alias="allowLiveShare", default=None,)
	allowMeetingChat: Optional[MeetingChatMode | str] = Field(alias="allowMeetingChat", default=None,)
	allowParticipantsToChangeName: Optional[bool] = Field(alias="allowParticipantsToChangeName", default=None,)
	allowPowerPointSharing: Optional[bool] = Field(alias="allowPowerPointSharing", default=None,)
	allowRecording: Optional[bool] = Field(alias="allowRecording", default=None,)
	allowTeamworkReactions: Optional[bool] = Field(alias="allowTeamworkReactions", default=None,)
	allowTranscription: Optional[bool] = Field(alias="allowTranscription", default=None,)
	allowWhiteboard: Optional[bool] = Field(alias="allowWhiteboard", default=None,)
	anonymizeIdentityForRoles: Optional[list[OnlineMeetingRole | str]] = Field(alias="anonymizeIdentityForRoles", default=None,)
	audioConferencing: Optional[AudioConferencing] = Field(alias="audioConferencing", default=None,)
	chatInfo: Optional[ChatInfo] = Field(alias="chatInfo", default=None,)
	chatRestrictions: Optional[ChatRestrictions] = Field(alias="chatRestrictions", default=None,)
	isEndToEndEncryptionEnabled: Optional[bool] = Field(alias="isEndToEndEncryptionEnabled", default=None,)
	isEntryExitAnnounced: Optional[bool] = Field(alias="isEntryExitAnnounced", default=None,)
	joinInformation: Optional[ItemBody] = Field(alias="joinInformation", default=None,)
	joinMeetingIdSettings: Optional[JoinMeetingIdSettings] = Field(alias="joinMeetingIdSettings", default=None,)
	joinWebUrl: Optional[str] = Field(alias="joinWebUrl", default=None,)
	lobbyBypassSettings: Optional[LobbyBypassSettings] = Field(alias="lobbyBypassSettings", default=None,)
	recordAutomatically: Optional[bool] = Field(alias="recordAutomatically", default=None,)
	shareMeetingChatHistoryDefault: Optional[MeetingChatHistoryDefaultMode | str] = Field(alias="shareMeetingChatHistoryDefault", default=None,)
	subject: Optional[str] = Field(alias="subject", default=None,)
	videoTeleconferenceId: Optional[str] = Field(alias="videoTeleconferenceId", default=None,)
	watermarkProtection: Optional[WatermarkProtectionValues] = Field(alias="watermarkProtection", default=None,)
	attendanceReports: Optional[list[MeetingAttendanceReport]] = Field(alias="attendanceReports", default=None,)
	alternativeRecording: Optional[str] = Field(alias="alternativeRecording", default=None,)
	attendeeReport: Optional[str] = Field(alias="attendeeReport", default=None,)
	broadcastRecording: Optional[str] = Field(alias="broadcastRecording", default=None,)
	broadcastSettings: Optional[BroadcastMeetingSettings] = Field(alias="broadcastSettings", default=None,)
	capabilities: Optional[list[MeetingCapabilities | str]] = Field(alias="capabilities", default=None,)
	creationDateTime: Optional[datetime] = Field(alias="creationDateTime", default=None,)
	endDateTime: Optional[datetime] = Field(alias="endDateTime", default=None,)
	externalId: Optional[str] = Field(alias="externalId", default=None,)
	isBroadcast: Optional[bool] = Field(alias="isBroadcast", default=None,)
	joinUrl: Optional[str] = Field(alias="joinUrl", default=None,)
	meetingTemplateId: Optional[str] = Field(alias="meetingTemplateId", default=None,)
	participants: Optional[MeetingParticipants] = Field(alias="participants", default=None,)
	recording: Optional[str] = Field(alias="recording", default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime", default=None,)
	aiInsights: Optional[list[CallAiInsight]] = Field(alias="aiInsights", default=None,)
	meetingAttendanceReport: Optional[MeetingAttendanceReport] = Field(alias="meetingAttendanceReport", default=None,)
	recordings: Optional[list[CallRecording]] = Field(alias="recordings", default=None,)
	registration: Optional[MeetingRegistration] = Field(alias="registration", default=None,)
	transcripts: Optional[list[CallTranscript]] = Field(alias="transcripts", default=None,)

from .allowed_lobby_admitter_roles import AllowedLobbyAdmitterRoles
from .online_meeting_presenters import OnlineMeetingPresenters
from .meeting_live_share_options import MeetingLiveShareOptions
from .meeting_chat_mode import MeetingChatMode
from .online_meeting_role import OnlineMeetingRole
from .audio_conferencing import AudioConferencing
from .chat_info import ChatInfo
from .chat_restrictions import ChatRestrictions
from .item_body import ItemBody
from .join_meeting_id_settings import JoinMeetingIdSettings
from .lobby_bypass_settings import LobbyBypassSettings
from .meeting_chat_history_default_mode import MeetingChatHistoryDefaultMode
from .watermark_protection_values import WatermarkProtectionValues
from .meeting_attendance_report import MeetingAttendanceReport
from .broadcast_meeting_settings import BroadcastMeetingSettings
from .meeting_capabilities import MeetingCapabilities
from .meeting_participants import MeetingParticipants
from .call_ai_insight import CallAiInsight
from .call_recording import CallRecording
from .meeting_registration import MeetingRegistration
from .call_transcript import CallTranscript

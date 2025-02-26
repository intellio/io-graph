from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from pydantic import BaseModel, Field


class OnlineMeetingBase(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	allowAttendeeToEnableCamera: Optional[bool] = Field(default=None,alias="allowAttendeeToEnableCamera",)
	allowAttendeeToEnableMic: Optional[bool] = Field(default=None,alias="allowAttendeeToEnableMic",)
	allowBreakoutRooms: Optional[bool] = Field(default=None,alias="allowBreakoutRooms",)
	allowedLobbyAdmitters: Optional[AllowedLobbyAdmitterRoles] = Field(default=None,alias="allowedLobbyAdmitters",)
	allowedPresenters: Optional[OnlineMeetingPresenters] = Field(default=None,alias="allowedPresenters",)
	allowLiveShare: Optional[MeetingLiveShareOptions] = Field(default=None,alias="allowLiveShare",)
	allowMeetingChat: Optional[MeetingChatMode] = Field(default=None,alias="allowMeetingChat",)
	allowParticipantsToChangeName: Optional[bool] = Field(default=None,alias="allowParticipantsToChangeName",)
	allowPowerPointSharing: Optional[bool] = Field(default=None,alias="allowPowerPointSharing",)
	allowRecording: Optional[bool] = Field(default=None,alias="allowRecording",)
	allowTeamworkReactions: Optional[bool] = Field(default=None,alias="allowTeamworkReactions",)
	allowTranscription: Optional[bool] = Field(default=None,alias="allowTranscription",)
	allowWhiteboard: Optional[bool] = Field(default=None,alias="allowWhiteboard",)
	audioConferencing: Optional[AudioConferencing] = Field(default=None,alias="audioConferencing",)
	chatInfo: Optional[ChatInfo] = Field(default=None,alias="chatInfo",)
	chatRestrictions: Optional[ChatRestrictions] = Field(default=None,alias="chatRestrictions",)
	isEntryExitAnnounced: Optional[bool] = Field(default=None,alias="isEntryExitAnnounced",)
	joinInformation: Optional[ItemBody] = Field(default=None,alias="joinInformation",)
	joinMeetingIdSettings: Optional[JoinMeetingIdSettings] = Field(default=None,alias="joinMeetingIdSettings",)
	joinWebUrl: Optional[str] = Field(default=None,alias="joinWebUrl",)
	lobbyBypassSettings: Optional[LobbyBypassSettings] = Field(default=None,alias="lobbyBypassSettings",)
	recordAutomatically: Optional[bool] = Field(default=None,alias="recordAutomatically",)
	shareMeetingChatHistoryDefault: Optional[MeetingChatHistoryDefaultMode] = Field(default=None,alias="shareMeetingChatHistoryDefault",)
	subject: Optional[str] = Field(default=None,alias="subject",)
	videoTeleconferenceId: Optional[str] = Field(default=None,alias="videoTeleconferenceId",)
	watermarkProtection: Optional[WatermarkProtectionValues] = Field(default=None,alias="watermarkProtection",)
	attendanceReports: list[MeetingAttendanceReport] = Field(alias="attendanceReports",)

	@model_validator(mode="wrap")
	def convert_discriminator_class(cls, data: Any, handler: ModelWrapValidatorHandler[Self]) -> Self:
		try:
			# check with parent model to catch any errors
			parent_validated_model = handler(data)
			# check if the discriminator field is present
			if "@odata.type" not in data:
				return parent_validated_model
			# get the discriminator value
			mapping_key = data["@odata.type"]
			if mapping_key == "#microsoft.graph.onlineMeeting":
				from .online_meeting import OnlineMeeting
				return OnlineMeeting.model_validate(data)
			if mapping_key == "#microsoft.graph.virtualEventSession":
				from .virtual_event_session import VirtualEventSession
				return VirtualEventSession.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .allowed_lobby_admitter_roles import AllowedLobbyAdmitterRoles
from .online_meeting_presenters import OnlineMeetingPresenters
from .meeting_live_share_options import MeetingLiveShareOptions
from .meeting_chat_mode import MeetingChatMode
from .audio_conferencing import AudioConferencing
from .chat_info import ChatInfo
from .chat_restrictions import ChatRestrictions
from .item_body import ItemBody
from .join_meeting_id_settings import JoinMeetingIdSettings
from .lobby_bypass_settings import LobbyBypassSettings
from .meeting_chat_history_default_mode import MeetingChatHistoryDefaultMode
from .watermark_protection_values import WatermarkProtectionValues
from .meeting_attendance_report import MeetingAttendanceReport


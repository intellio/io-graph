from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class OnlineMeetingBase(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	allowAttendeeToEnableCamera: Optional[bool] = Field(alias="allowAttendeeToEnableCamera",default=None,)
	allowAttendeeToEnableMic: Optional[bool] = Field(alias="allowAttendeeToEnableMic",default=None,)
	allowBreakoutRooms: Optional[bool] = Field(alias="allowBreakoutRooms",default=None,)
	allowedLobbyAdmitters: Optional[AllowedLobbyAdmitterRoles | str] = Field(alias="allowedLobbyAdmitters",default=None,)
	allowedPresenters: Optional[OnlineMeetingPresenters | str] = Field(alias="allowedPresenters",default=None,)
	allowLiveShare: Optional[MeetingLiveShareOptions | str] = Field(alias="allowLiveShare",default=None,)
	allowMeetingChat: Optional[MeetingChatMode | str] = Field(alias="allowMeetingChat",default=None,)
	allowParticipantsToChangeName: Optional[bool] = Field(alias="allowParticipantsToChangeName",default=None,)
	allowPowerPointSharing: Optional[bool] = Field(alias="allowPowerPointSharing",default=None,)
	allowRecording: Optional[bool] = Field(alias="allowRecording",default=None,)
	allowTeamworkReactions: Optional[bool] = Field(alias="allowTeamworkReactions",default=None,)
	allowTranscription: Optional[bool] = Field(alias="allowTranscription",default=None,)
	allowWhiteboard: Optional[bool] = Field(alias="allowWhiteboard",default=None,)
	anonymizeIdentityForRoles: Optional[OnlineMeetingRole | str] = Field(alias="anonymizeIdentityForRoles",default=None,)
	audioConferencing: Optional[AudioConferencing] = Field(alias="audioConferencing",default=None,)
	chatInfo: Optional[ChatInfo] = Field(alias="chatInfo",default=None,)
	chatRestrictions: Optional[ChatRestrictions] = Field(alias="chatRestrictions",default=None,)
	isEndToEndEncryptionEnabled: Optional[bool] = Field(alias="isEndToEndEncryptionEnabled",default=None,)
	isEntryExitAnnounced: Optional[bool] = Field(alias="isEntryExitAnnounced",default=None,)
	joinInformation: Optional[ItemBody] = Field(alias="joinInformation",default=None,)
	joinMeetingIdSettings: Optional[JoinMeetingIdSettings] = Field(alias="joinMeetingIdSettings",default=None,)
	joinWebUrl: Optional[str] = Field(alias="joinWebUrl",default=None,)
	lobbyBypassSettings: Optional[LobbyBypassSettings] = Field(alias="lobbyBypassSettings",default=None,)
	recordAutomatically: Optional[bool] = Field(alias="recordAutomatically",default=None,)
	shareMeetingChatHistoryDefault: Optional[MeetingChatHistoryDefaultMode | str] = Field(alias="shareMeetingChatHistoryDefault",default=None,)
	subject: Optional[str] = Field(alias="subject",default=None,)
	videoTeleconferenceId: Optional[str] = Field(alias="videoTeleconferenceId",default=None,)
	watermarkProtection: Optional[WatermarkProtectionValues] = Field(alias="watermarkProtection",default=None,)
	attendanceReports: Optional[list[MeetingAttendanceReport]] = Field(alias="attendanceReports",default=None,)

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


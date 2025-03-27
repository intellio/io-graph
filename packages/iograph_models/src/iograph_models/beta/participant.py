from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Participant(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	info: Optional[ParticipantInfo] = Field(alias="info", default=None,)
	isIdentityAnonymized: Optional[bool] = Field(alias="isIdentityAnonymized", default=None,)
	isInLobby: Optional[bool] = Field(alias="isInLobby", default=None,)
	isMuted: Optional[bool] = Field(alias="isMuted", default=None,)
	mediaStreams: Optional[list[MediaStream]] = Field(alias="mediaStreams", default=None,)
	metadata: Optional[str] = Field(alias="metadata", default=None,)
	preferredDisplayName: Optional[str] = Field(alias="preferredDisplayName", default=None,)
	recordingInfo: Optional[RecordingInfo] = Field(alias="recordingInfo", default=None,)
	removedState: Optional[RemovedState] = Field(alias="removedState", default=None,)
	restrictedExperience: Optional[OnlineMeetingRestricted] = Field(alias="restrictedExperience", default=None,)
	rosterSequenceNumber: Optional[int] = Field(alias="rosterSequenceNumber", default=None,)

from .participant_info import ParticipantInfo
from .media_stream import MediaStream
from .recording_info import RecordingInfo
from .removed_state import RemovedState
from .online_meeting_restricted import OnlineMeetingRestricted


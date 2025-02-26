from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Participant(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	info: Optional[ParticipantInfo] = Field(default=None,alias="info",)
	isInLobby: Optional[bool] = Field(default=None,alias="isInLobby",)
	isMuted: Optional[bool] = Field(default=None,alias="isMuted",)
	mediaStreams: list[MediaStream] = Field(alias="mediaStreams",)
	metadata: Optional[str] = Field(default=None,alias="metadata",)
	recordingInfo: Optional[RecordingInfo] = Field(default=None,alias="recordingInfo",)
	removedState: Optional[RemovedState] = Field(default=None,alias="removedState",)
	restrictedExperience: Optional[OnlineMeetingRestricted] = Field(default=None,alias="restrictedExperience",)
	rosterSequenceNumber: Optional[int] = Field(default=None,alias="rosterSequenceNumber",)

from .participant_info import ParticipantInfo
from .media_stream import MediaStream
from .recording_info import RecordingInfo
from .removed_state import RemovedState
from .online_meeting_restricted import OnlineMeetingRestricted


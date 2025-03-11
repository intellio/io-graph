from __future__ import annotations
from enum import StrEnum


class MeetingMessageType(StrEnum):
	none = "none"
	meetingRequest = "meetingRequest"
	meetingCancelled = "meetingCancelled"
	meetingAccepted = "meetingAccepted"
	meetingTentativelyAccepted = "meetingTentativelyAccepted"
	meetingDeclined = "meetingDeclined"


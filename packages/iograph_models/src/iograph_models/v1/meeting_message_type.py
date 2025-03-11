from __future__ import annotations
from enum import StrEnum


class MeetingMessageType(StrEnum):
	none = "none"
	meetingRequest = "meetingRequest"
	meetingCancelled = "meetingCancelled"
	meetingAccepted = "meetingAccepted"
	meetingTenativelyAccepted = "meetingTenativelyAccepted"
	meetingDeclined = "meetingDeclined"


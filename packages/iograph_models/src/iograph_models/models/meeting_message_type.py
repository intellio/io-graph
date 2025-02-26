from __future__ import annotations
from enum import Enum


class MeetingMessageType(Enum):
	none = "none"
	meetingRequest = "meetingRequest"
	meetingCancelled = "meetingCancelled"
	meetingAccepted = "meetingAccepted"
	meetingTenativelyAccepted = "meetingTenativelyAccepted"
	meetingDeclined = "meetingDeclined"


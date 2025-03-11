from __future__ import annotations
from enum import StrEnum


class BroadcastMeetingAudience(StrEnum):
	roleIsAttendee = "roleIsAttendee"
	organization = "organization"
	everyone = "everyone"
	unknownFutureValue = "unknownFutureValue"


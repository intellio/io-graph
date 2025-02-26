from __future__ import annotations
from enum import Enum


class BroadcastMeetingAudience(Enum):
	roleIsAttendee = "roleIsAttendee"
	organization = "organization"
	everyone = "everyone"
	unknownFutureValue = "unknownFutureValue"


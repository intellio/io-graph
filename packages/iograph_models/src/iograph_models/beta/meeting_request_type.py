from __future__ import annotations
from enum import StrEnum


class MeetingRequestType(StrEnum):
	none = "none"
	newMeetingRequest = "newMeetingRequest"
	fullUpdate = "fullUpdate"
	informationalUpdate = "informationalUpdate"
	silentUpdate = "silentUpdate"
	outdated = "outdated"
	principalWantsCopy = "principalWantsCopy"


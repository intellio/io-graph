from __future__ import annotations
from enum import Enum


class MeetingRequestType(Enum):
	none = "none"
	newMeetingRequest = "newMeetingRequest"
	fullUpdate = "fullUpdate"
	informationalUpdate = "informationalUpdate"
	silentUpdate = "silentUpdate"
	outdated = "outdated"
	principalWantsCopy = "principalWantsCopy"


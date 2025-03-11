from __future__ import annotations
from enum import StrEnum


class CallEventType(StrEnum):
	callStarted = "callStarted"
	callEnded = "callEnded"
	unknownFutureValue = "unknownFutureValue"
	rosterUpdated = "rosterUpdated"


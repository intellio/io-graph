from __future__ import annotations
from enum import Enum


class CallTranscriptionState(Enum):
	notStarted = "notStarted"
	active = "active"
	inactive = "inactive"
	unknownFutureValue = "unknownFutureValue"


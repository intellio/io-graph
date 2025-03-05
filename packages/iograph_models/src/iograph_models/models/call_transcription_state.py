from __future__ import annotations
from enum import StrEnum


class CallTranscriptionState(StrEnum):
	notStarted = "notStarted"
	active = "active"
	inactive = "inactive"
	unknownFutureValue = "unknownFutureValue"


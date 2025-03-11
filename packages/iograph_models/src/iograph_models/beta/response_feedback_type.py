from __future__ import annotations
from enum import StrEnum


class ResponseFeedbackType(StrEnum):
	none = "none"
	notDetected = "notDetected"
	veryUnpleasant = "veryUnpleasant"
	unpleasant = "unpleasant"
	neutral = "neutral"
	pleasant = "pleasant"
	veryPleasant = "veryPleasant"
	unknownFutureValue = "unknownFutureValue"


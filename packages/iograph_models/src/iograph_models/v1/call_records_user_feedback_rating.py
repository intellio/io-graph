from __future__ import annotations
from enum import StrEnum


class CallRecordsUserFeedbackRating(StrEnum):
	notRated = "notRated"
	bad = "bad"
	poor = "poor"
	fair = "fair"
	good = "good"
	excellent = "excellent"
	unknownFutureValue = "unknownFutureValue"


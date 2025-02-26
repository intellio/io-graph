from __future__ import annotations
from enum import Enum


class CallRecordsUserFeedbackRating(Enum):
	notRated = "notRated"
	bad = "bad"
	poor = "poor"
	fair = "fair"
	good = "good"
	excellent = "excellent"
	unknownFutureValue = "unknownFutureValue"


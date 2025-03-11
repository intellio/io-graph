from __future__ import annotations
from enum import StrEnum


class AlertFeedback(StrEnum):
	unknown = "unknown"
	truePositive = "truePositive"
	falsePositive = "falsePositive"
	benignPositive = "benignPositive"
	unknownFutureValue = "unknownFutureValue"


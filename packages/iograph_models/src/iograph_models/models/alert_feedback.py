from __future__ import annotations
from enum import Enum


class AlertFeedback(Enum):
	unknown = "unknown"
	truePositive = "truePositive"
	falsePositive = "falsePositive"
	benignPositive = "benignPositive"
	unknownFutureValue = "unknownFutureValue"


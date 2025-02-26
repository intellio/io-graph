from __future__ import annotations
from enum import Enum


class SecurityAlertClassification(Enum):
	unknown = "unknown"
	falsePositive = "falsePositive"
	truePositive = "truePositive"
	informationalExpectedActivity = "informationalExpectedActivity"
	unknownFutureValue = "unknownFutureValue"


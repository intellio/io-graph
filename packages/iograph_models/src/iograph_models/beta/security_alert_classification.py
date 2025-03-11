from __future__ import annotations
from enum import StrEnum


class SecurityAlertClassification(StrEnum):
	unknown = "unknown"
	falsePositive = "falsePositive"
	truePositive = "truePositive"
	informationalExpectedActivity = "informationalExpectedActivity"
	unknownFutureValue = "unknownFutureValue"


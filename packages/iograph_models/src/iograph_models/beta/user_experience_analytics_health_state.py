from __future__ import annotations
from enum import StrEnum


class UserExperienceAnalyticsHealthState(StrEnum):
	unknown = "unknown"
	insufficientData = "insufficientData"
	needsAttention = "needsAttention"
	meetingGoals = "meetingGoals"
	unknownFutureValue = "unknownFutureValue"


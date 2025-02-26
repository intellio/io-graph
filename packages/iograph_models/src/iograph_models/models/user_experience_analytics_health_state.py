from __future__ import annotations
from enum import Enum


class UserExperienceAnalyticsHealthState(Enum):
	unknown = "unknown"
	insufficientData = "insufficientData"
	needsAttention = "needsAttention"
	meetingGoals = "meetingGoals"
	unknownFutureValue = "unknownFutureValue"


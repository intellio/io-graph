from __future__ import annotations
from enum import StrEnum


class UserExperienceAnalyticsAnomalyState(StrEnum):
	new = "new"
	active = "active"
	disabled = "disabled"
	removed = "removed"
	other = "other"
	unknownFutureValue = "unknownFutureValue"


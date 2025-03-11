from __future__ import annotations
from enum import StrEnum


class SecurityAlertStatus(StrEnum):
	unknown = "unknown"
	new = "new"
	inProgress = "inProgress"
	resolved = "resolved"
	unknownFutureValue = "unknownFutureValue"


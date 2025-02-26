from __future__ import annotations
from enum import Enum


class SecurityAlertStatus(Enum):
	unknown = "unknown"
	new = "new"
	inProgress = "inProgress"
	resolved = "resolved"
	unknownFutureValue = "unknownFutureValue"


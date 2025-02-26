from __future__ import annotations
from enum import Enum


class AlertStatus(Enum):
	unknown = "unknown"
	newAlert = "newAlert"
	inProgress = "inProgress"
	resolved = "resolved"
	dismissed = "dismissed"
	unknownFutureValue = "unknownFutureValue"


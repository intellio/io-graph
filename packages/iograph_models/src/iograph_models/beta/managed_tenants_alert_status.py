from __future__ import annotations
from enum import StrEnum


class ManagedTenantsAlertStatus(StrEnum):
	unknown = "unknown"
	newAlert = "newAlert"
	inProgress = "inProgress"
	resolved = "resolved"
	dismissed = "dismissed"
	unknownFutureValue = "unknownFutureValue"


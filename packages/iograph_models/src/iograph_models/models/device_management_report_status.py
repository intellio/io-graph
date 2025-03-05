from __future__ import annotations
from enum import StrEnum


class DeviceManagementReportStatus(StrEnum):
	unknown = "unknown"
	notStarted = "notStarted"
	inProgress = "inProgress"
	completed = "completed"
	failed = "failed"


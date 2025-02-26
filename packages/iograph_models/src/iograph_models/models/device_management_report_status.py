from __future__ import annotations
from enum import Enum


class DeviceManagementReportStatus(Enum):
	unknown = "unknown"
	notStarted = "notStarted"
	inProgress = "inProgress"
	completed = "completed"
	failed = "failed"


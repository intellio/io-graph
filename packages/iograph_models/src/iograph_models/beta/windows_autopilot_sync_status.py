from __future__ import annotations
from enum import StrEnum


class WindowsAutopilotSyncStatus(StrEnum):
	unknown = "unknown"
	inProgress = "inProgress"
	completed = "completed"
	failed = "failed"


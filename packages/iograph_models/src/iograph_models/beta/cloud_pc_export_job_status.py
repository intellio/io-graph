from __future__ import annotations
from enum import StrEnum


class CloudPcExportJobStatus(StrEnum):
	notStarted = "notStarted"
	inProgress = "inProgress"
	completed = "completed"
	failed = "failed"
	unknownFutureValue = "unknownFutureValue"


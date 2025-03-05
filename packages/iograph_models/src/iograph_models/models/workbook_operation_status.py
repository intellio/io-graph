from __future__ import annotations
from enum import StrEnum


class WorkbookOperationStatus(StrEnum):
	notStarted = "notStarted"
	running = "running"
	succeeded = "succeeded"
	failed = "failed"


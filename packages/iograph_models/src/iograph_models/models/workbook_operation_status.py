from __future__ import annotations
from enum import Enum


class WorkbookOperationStatus(Enum):
	notStarted = "notStarted"
	running = "running"
	succeeded = "succeeded"
	failed = "failed"


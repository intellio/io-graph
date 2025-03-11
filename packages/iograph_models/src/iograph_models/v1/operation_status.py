from __future__ import annotations
from enum import StrEnum


class OperationStatus(StrEnum):
	NotStarted = "NotStarted"
	Running = "Running"
	Completed = "Completed"
	Failed = "Failed"


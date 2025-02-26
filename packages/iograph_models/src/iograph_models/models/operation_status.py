from __future__ import annotations
from enum import Enum


class OperationStatus(Enum):
	NotStarted = "NotStarted"
	Running = "Running"
	Completed = "Completed"
	Failed = "Failed"


from __future__ import annotations
from enum import StrEnum


class ConnectionOperationStatus(StrEnum):
	unspecified = "unspecified"
	inprogress = "inprogress"
	completed = "completed"
	failed = "failed"


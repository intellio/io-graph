from __future__ import annotations
from enum import Enum


class EntryExportStatus(Enum):
	Noop = "Noop"
	Success = "Success"
	RetryableError = "RetryableError"
	PermanentError = "PermanentError"
	Error = "Error"


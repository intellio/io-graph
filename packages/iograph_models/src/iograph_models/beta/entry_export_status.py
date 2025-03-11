from __future__ import annotations
from enum import StrEnum


class EntryExportStatus(StrEnum):
	Noop = "Noop"
	Success = "Success"
	RetryableError = "RetryableError"
	PermanentError = "PermanentError"
	Error = "Error"


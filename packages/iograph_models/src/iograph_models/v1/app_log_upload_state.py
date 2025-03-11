from __future__ import annotations
from enum import StrEnum


class AppLogUploadState(StrEnum):
	pending = "pending"
	completed = "completed"
	failed = "failed"
	unknownFutureValue = "unknownFutureValue"


from __future__ import annotations
from enum import Enum


class AppLogUploadState(Enum):
	pending = "pending"
	completed = "completed"
	failed = "failed"
	unknownFutureValue = "unknownFutureValue"


from __future__ import annotations
from enum import StrEnum


class ConnectionStatus(StrEnum):
	unknown = "unknown"
	attempted = "attempted"
	succeeded = "succeeded"
	blocked = "blocked"
	failed = "failed"
	unknownFutureValue = "unknownFutureValue"


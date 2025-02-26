from __future__ import annotations
from enum import Enum


class ConnectionStatus(Enum):
	unknown = "unknown"
	attempted = "attempted"
	succeeded = "succeeded"
	blocked = "blocked"
	failed = "failed"
	unknownFutureValue = "unknownFutureValue"


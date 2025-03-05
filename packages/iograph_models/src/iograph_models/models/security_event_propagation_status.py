from __future__ import annotations
from enum import StrEnum


class SecurityEventPropagationStatus(StrEnum):
	none = "none"
	inProcessing = "inProcessing"
	failed = "failed"
	success = "success"
	unknownFutureValue = "unknownFutureValue"


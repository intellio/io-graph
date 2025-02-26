from __future__ import annotations
from enum import Enum


class SecurityEventPropagationStatus(Enum):
	none = "none"
	inProcessing = "inProcessing"
	failed = "failed"
	success = "success"
	unknownFutureValue = "unknownFutureValue"


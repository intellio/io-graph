from __future__ import annotations
from enum import StrEnum


class RemediationState(StrEnum):
	unknown = "unknown"
	skipped = "skipped"
	success = "success"
	remediationFailed = "remediationFailed"
	scriptError = "scriptError"
	unknownFutureValue = "unknownFutureValue"


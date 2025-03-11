from __future__ import annotations
from enum import StrEnum


class IndustryDataReadinessStatus(StrEnum):
	notReady = "notReady"
	ready = "ready"
	failed = "failed"
	disabled = "disabled"
	expired = "expired"
	unknownFutureValue = "unknownFutureValue"


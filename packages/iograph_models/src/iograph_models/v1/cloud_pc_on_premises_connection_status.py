from __future__ import annotations
from enum import StrEnum


class CloudPcOnPremisesConnectionStatus(StrEnum):
	pending = "pending"
	running = "running"
	passed = "passed"
	failed = "failed"
	warning = "warning"
	informational = "informational"
	unknownFutureValue = "unknownFutureValue"


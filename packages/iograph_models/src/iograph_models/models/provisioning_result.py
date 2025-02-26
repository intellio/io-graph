from __future__ import annotations
from enum import Enum


class ProvisioningResult(Enum):
	success = "success"
	failure = "failure"
	skipped = "skipped"
	warning = "warning"
	unknownFutureValue = "unknownFutureValue"


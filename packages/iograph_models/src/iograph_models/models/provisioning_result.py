from __future__ import annotations
from enum import StrEnum


class ProvisioningResult(StrEnum):
	success = "success"
	failure = "failure"
	skipped = "skipped"
	warning = "warning"
	unknownFutureValue = "unknownFutureValue"


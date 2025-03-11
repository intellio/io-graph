from __future__ import annotations
from enum import StrEnum


class DeviceScopeActionStatus(StrEnum):
	failed = "failed"
	succeeded = "succeeded"
	unknownFutureValue = "unknownFutureValue"


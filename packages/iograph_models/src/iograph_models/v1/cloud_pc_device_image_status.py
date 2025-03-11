from __future__ import annotations
from enum import StrEnum


class CloudPcDeviceImageStatus(StrEnum):
	pending = "pending"
	ready = "ready"
	failed = "failed"
	unknownFutureValue = "unknownFutureValue"


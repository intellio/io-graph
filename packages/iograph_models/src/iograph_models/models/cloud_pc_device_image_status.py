from __future__ import annotations
from enum import Enum


class CloudPcDeviceImageStatus(Enum):
	pending = "pending"
	ready = "ready"
	failed = "failed"
	unknownFutureValue = "unknownFutureValue"


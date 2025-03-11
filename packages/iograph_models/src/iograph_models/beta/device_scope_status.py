from __future__ import annotations
from enum import StrEnum


class DeviceScopeStatus(StrEnum):
	none = "none"
	computing = "computing"
	insufficientData = "insufficientData"
	completed = "completed"
	unknownFutureValue = "unknownFutureValue"


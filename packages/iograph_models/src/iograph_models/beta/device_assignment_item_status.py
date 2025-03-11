from __future__ import annotations
from enum import StrEnum


class DeviceAssignmentItemStatus(StrEnum):
	initiated = "initiated"
	inProgress = "inProgress"
	removed = "removed"
	error = "error"
	succeeded = "succeeded"
	unknownFutureValue = "unknownFutureValue"


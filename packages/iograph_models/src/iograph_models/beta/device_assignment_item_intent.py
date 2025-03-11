from __future__ import annotations
from enum import StrEnum


class DeviceAssignmentItemIntent(StrEnum):
	remove = "remove"
	restore = "restore"
	unknownFutureValue = "unknownFutureValue"


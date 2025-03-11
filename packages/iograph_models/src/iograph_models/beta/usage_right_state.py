from __future__ import annotations
from enum import StrEnum


class UsageRightState(StrEnum):
	active = "active"
	inactive = "inactive"
	warning = "warning"
	suspended = "suspended"
	unknownFutureValue = "unknownFutureValue"


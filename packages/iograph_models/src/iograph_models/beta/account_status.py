from __future__ import annotations
from enum import StrEnum


class AccountStatus(StrEnum):
	unknown = "unknown"
	staged = "staged"
	active = "active"
	suspended = "suspended"
	deleted = "deleted"
	unknownFutureValue = "unknownFutureValue"


from __future__ import annotations
from enum import StrEnum


class Status(StrEnum):
	active = "active"
	updated = "updated"
	deleted = "deleted"
	ignored = "ignored"
	unknownFutureValue = "unknownFutureValue"


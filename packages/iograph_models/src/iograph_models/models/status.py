from __future__ import annotations
from enum import Enum


class Status(Enum):
	active = "active"
	updated = "updated"
	deleted = "deleted"
	ignored = "ignored"
	unknownFutureValue = "unknownFutureValue"


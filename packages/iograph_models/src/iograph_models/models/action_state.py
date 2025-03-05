from __future__ import annotations
from enum import StrEnum


class ActionState(StrEnum):
	none = "none"
	pending = "pending"
	canceled = "canceled"
	active = "active"
	done = "done"
	failed = "failed"
	notSupported = "notSupported"


from __future__ import annotations
from enum import Enum


class ActionState(Enum):
	none = "none"
	pending = "pending"
	canceled = "canceled"
	active = "active"
	done = "done"
	failed = "failed"
	notSupported = "notSupported"


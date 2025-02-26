from __future__ import annotations
from enum import Enum


class SiteLockState(Enum):
	unlocked = "unlocked"
	lockedReadOnly = "lockedReadOnly"
	lockedNoAccess = "lockedNoAccess"
	lockedNoAdditions = "lockedNoAdditions"
	unknownFutureValue = "unknownFutureValue"


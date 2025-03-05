from __future__ import annotations
from enum import StrEnum


class SiteLockState(StrEnum):
	unlocked = "unlocked"
	lockedReadOnly = "lockedReadOnly"
	lockedNoAccess = "lockedNoAccess"
	lockedNoAdditions = "lockedNoAdditions"
	unknownFutureValue = "unknownFutureValue"


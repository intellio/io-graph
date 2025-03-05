from __future__ import annotations
from enum import StrEnum


class IdentityGovernanceLifecycleTaskCategory(StrEnum):
	joiner = "joiner"
	leaver = "leaver"
	unknownFutureValue = "unknownFutureValue"
	mover = "mover"


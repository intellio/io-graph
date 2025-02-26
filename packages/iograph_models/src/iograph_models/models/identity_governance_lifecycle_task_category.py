from __future__ import annotations
from enum import Enum


class IdentityGovernanceLifecycleTaskCategory(Enum):
	joiner = "joiner"
	leaver = "leaver"
	unknownFutureValue = "unknownFutureValue"
	mover = "mover"


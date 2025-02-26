from __future__ import annotations
from enum import Enum


class IdentityGovernanceLifecycleWorkflowCategory(Enum):
	joiner = "joiner"
	leaver = "leaver"
	unknownFutureValue = "unknownFutureValue"
	mover = "mover"


from __future__ import annotations
from enum import StrEnum


class IdentityGovernanceLifecycleWorkflowCategory(StrEnum):
	joiner = "joiner"
	leaver = "leaver"
	unknownFutureValue = "unknownFutureValue"
	mover = "mover"


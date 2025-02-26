from __future__ import annotations
from enum import Enum


class ChatMessagePolicyViolationUserActionTypes(Enum):
	none = "none"
	override = "override"
	reportFalsePositive = "reportFalsePositive"


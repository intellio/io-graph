from __future__ import annotations
from enum import Enum


class ChatMessagePolicyViolationVerdictDetailsTypes(Enum):
	none = "none"
	allowFalsePositiveOverride = "allowFalsePositiveOverride"
	allowOverrideWithoutJustification = "allowOverrideWithoutJustification"
	allowOverrideWithJustification = "allowOverrideWithJustification"


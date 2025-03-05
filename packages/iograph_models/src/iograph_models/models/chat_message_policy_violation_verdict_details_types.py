from __future__ import annotations
from enum import StrEnum


class ChatMessagePolicyViolationVerdictDetailsTypes(StrEnum):
	none = "none"
	allowFalsePositiveOverride = "allowFalsePositiveOverride"
	allowOverrideWithoutJustification = "allowOverrideWithoutJustification"
	allowOverrideWithJustification = "allowOverrideWithJustification"


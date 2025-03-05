from __future__ import annotations
from enum import StrEnum


class ChatMessagePolicyViolationUserActionTypes(StrEnum):
	none = "none"
	override = "override"
	reportFalsePositive = "reportFalsePositive"


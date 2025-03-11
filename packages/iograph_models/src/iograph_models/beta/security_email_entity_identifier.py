from __future__ import annotations
from enum import StrEnum


class SecurityEmailEntityIdentifier(StrEnum):
	networkMessageId = "networkMessageId"
	recipientEmailAddress = "recipientEmailAddress"
	unknownFutureValue = "unknownFutureValue"


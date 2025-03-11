from __future__ import annotations
from enum import StrEnum


class CoachmarkLocationType(StrEnum):
	unknown = "unknown"
	fromEmail = "fromEmail"
	subject = "subject"
	externalTag = "externalTag"
	displayName = "displayName"
	messageBody = "messageBody"
	unknownFutureValue = "unknownFutureValue"


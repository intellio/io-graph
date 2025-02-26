from __future__ import annotations
from enum import Enum


class CoachmarkLocationType(Enum):
	unknown = "unknown"
	fromEmail = "fromEmail"
	subject = "subject"
	externalTag = "externalTag"
	displayName = "displayName"
	messageBody = "messageBody"
	unknownFutureValue = "unknownFutureValue"


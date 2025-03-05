from __future__ import annotations
from enum import StrEnum


class VirtualEventRegistrationQuestionAnswerInputType(StrEnum):
	text = "text"
	multilineText = "multilineText"
	singleChoice = "singleChoice"
	multiChoice = "multiChoice"
	boolean = "boolean"
	unknownFutureValue = "unknownFutureValue"


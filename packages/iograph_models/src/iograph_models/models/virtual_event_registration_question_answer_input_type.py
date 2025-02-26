from __future__ import annotations
from enum import Enum


class VirtualEventRegistrationQuestionAnswerInputType(Enum):
	text = "text"
	multilineText = "multilineText"
	singleChoice = "singleChoice"
	multiChoice = "multiChoice"
	boolean = "boolean"
	unknownFutureValue = "unknownFutureValue"


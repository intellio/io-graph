from __future__ import annotations
from enum import StrEnum


class AnswerInputType(StrEnum):
	text = "text"
	radioButton = "radioButton"
	unknownFutureValue = "unknownFutureValue"


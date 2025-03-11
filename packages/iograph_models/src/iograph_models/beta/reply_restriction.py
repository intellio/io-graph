from __future__ import annotations
from enum import StrEnum


class ReplyRestriction(StrEnum):
	everyone = "everyone"
	authorAndModerators = "authorAndModerators"
	unknownFutureValue = "unknownFutureValue"


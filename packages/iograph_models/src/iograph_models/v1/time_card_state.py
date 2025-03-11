from __future__ import annotations
from enum import StrEnum


class TimeCardState(StrEnum):
	clockedIn = "clockedIn"
	onBreak = "onBreak"
	clockedOut = "clockedOut"
	unknownFutureValue = "unknownFutureValue"


from __future__ import annotations
from enum import Enum


class TimeCardState(Enum):
	clockedIn = "clockedIn"
	onBreak = "onBreak"
	clockedOut = "clockedOut"
	unknownFutureValue = "unknownFutureValue"


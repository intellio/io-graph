from __future__ import annotations
from enum import StrEnum


class CallRecordsPstnUserBlockMode(StrEnum):
	blocked = "blocked"
	unblocked = "unblocked"
	unknownFutureValue = "unknownFutureValue"


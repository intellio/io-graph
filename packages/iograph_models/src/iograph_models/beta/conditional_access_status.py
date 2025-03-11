from __future__ import annotations
from enum import StrEnum


class ConditionalAccessStatus(StrEnum):
	success = "success"
	failure = "failure"
	notApplied = "notApplied"
	unknownFutureValue = "unknownFutureValue"


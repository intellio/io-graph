from __future__ import annotations
from enum import Enum


class ConditionalAccessStatus(Enum):
	success = "success"
	failure = "failure"
	notApplied = "notApplied"
	unknownFutureValue = "unknownFutureValue"


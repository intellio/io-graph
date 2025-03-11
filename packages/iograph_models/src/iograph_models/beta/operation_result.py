from __future__ import annotations
from enum import StrEnum


class OperationResult(StrEnum):
	success = "success"
	failure = "failure"
	timeout = "timeout"
	unknownFutureValue = "unknownFutureValue"


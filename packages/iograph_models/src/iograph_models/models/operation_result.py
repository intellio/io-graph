from __future__ import annotations
from enum import Enum


class OperationResult(Enum):
	success = "success"
	failure = "failure"
	timeout = "timeout"
	unknownFutureValue = "unknownFutureValue"


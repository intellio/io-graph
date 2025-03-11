from __future__ import annotations
from enum import StrEnum


class AuthenticationAppEvaluation(StrEnum):
	success = "success"
	failure = "failure"
	unknownFutureValue = "unknownFutureValue"


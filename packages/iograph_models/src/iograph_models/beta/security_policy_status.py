from __future__ import annotations
from enum import StrEnum


class SecurityPolicyStatus(StrEnum):
	pending = "pending"
	error = "error"
	success = "success"
	unknownFutureValue = "unknownFutureValue"


from __future__ import annotations
from enum import StrEnum


class SecurityEventStatusType(StrEnum):
	pending = "pending"
	error = "error"
	success = "success"
	notAvaliable = "notAvaliable"
	unknownFutureValue = "unknownFutureValue"


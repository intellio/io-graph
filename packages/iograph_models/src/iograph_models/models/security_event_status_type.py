from __future__ import annotations
from enum import Enum


class SecurityEventStatusType(Enum):
	pending = "pending"
	error = "error"
	success = "success"
	notAvaliable = "notAvaliable"
	unknownFutureValue = "unknownFutureValue"


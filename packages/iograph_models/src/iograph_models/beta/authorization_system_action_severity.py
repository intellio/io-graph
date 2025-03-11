from __future__ import annotations
from enum import StrEnum


class AuthorizationSystemActionSeverity(StrEnum):
	normal = "normal"
	high = "high"
	unknownFutureValue = "unknownFutureValue"


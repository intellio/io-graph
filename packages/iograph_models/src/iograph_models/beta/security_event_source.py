from __future__ import annotations
from enum import StrEnum


class SecurityEventSource(StrEnum):
	system = "system"
	admin = "admin"
	user = "user"
	unknownFutureValue = "unknownFutureValue"


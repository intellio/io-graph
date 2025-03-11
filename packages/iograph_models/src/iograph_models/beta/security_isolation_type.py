from __future__ import annotations
from enum import StrEnum


class SecurityIsolationType(StrEnum):
	full = "full"
	selective = "selective"
	unknownFutureValue = "unknownFutureValue"


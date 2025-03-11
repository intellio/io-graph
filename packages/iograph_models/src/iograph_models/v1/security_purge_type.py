from __future__ import annotations
from enum import StrEnum


class SecurityPurgeType(StrEnum):
	recoverable = "recoverable"
	unknownFutureValue = "unknownFutureValue"
	permanentlyDelete = "permanentlyDelete"


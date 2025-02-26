from __future__ import annotations
from enum import Enum


class SecurityPurgeType(Enum):
	recoverable = "recoverable"
	unknownFutureValue = "unknownFutureValue"
	permanentlyDelete = "permanentlyDelete"


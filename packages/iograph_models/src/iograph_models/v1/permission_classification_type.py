from __future__ import annotations
from enum import StrEnum


class PermissionClassificationType(StrEnum):
	low = "low"
	medium = "medium"
	high = "high"
	unknownFutureValue = "unknownFutureValue"


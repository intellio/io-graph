from __future__ import annotations
from enum import StrEnum


class ProtectionSource(StrEnum):
	none = "none"
	manual = "manual"
	dynamicRule = "dynamicRule"
	unknownFutureValue = "unknownFutureValue"


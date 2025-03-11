from __future__ import annotations
from enum import StrEnum


class AdvancedConfigState(StrEnum):
	default = "default"
	enabled = "enabled"
	disabled = "disabled"
	unknownFutureValue = "unknownFutureValue"


from __future__ import annotations
from enum import Enum


class AdvancedConfigState(Enum):
	default = "default"
	enabled = "enabled"
	disabled = "disabled"
	unknownFutureValue = "unknownFutureValue"


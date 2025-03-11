from __future__ import annotations
from enum import StrEnum


class ActionCapability(StrEnum):
	enabled = "enabled"
	disabled = "disabled"
	unknownFutureValue = "unknownFutureValue"


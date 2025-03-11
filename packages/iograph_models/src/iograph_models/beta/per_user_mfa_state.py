from __future__ import annotations
from enum import StrEnum


class PerUserMfaState(StrEnum):
	disabled = "disabled"
	enforced = "enforced"
	enabled = "enabled"
	unknownFutureValue = "unknownFutureValue"


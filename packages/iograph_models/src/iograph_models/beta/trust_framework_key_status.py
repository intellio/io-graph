from __future__ import annotations
from enum import StrEnum


class TrustFrameworkKeyStatus(StrEnum):
	enabled = "enabled"
	disabled = "disabled"
	unknownFutureValue = "unknownFutureValue"


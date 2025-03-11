from __future__ import annotations
from enum import StrEnum


class ExternalEmailOtpState(StrEnum):
	default = "default"
	enabled = "enabled"
	disabled = "disabled"
	unknownFutureValue = "unknownFutureValue"


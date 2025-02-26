from __future__ import annotations
from enum import Enum


class ExternalEmailOtpState(Enum):
	default = "default"
	enabled = "enabled"
	disabled = "disabled"
	unknownFutureValue = "unknownFutureValue"


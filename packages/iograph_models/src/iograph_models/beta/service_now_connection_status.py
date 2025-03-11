from __future__ import annotations
from enum import StrEnum


class ServiceNowConnectionStatus(StrEnum):
	disabled = "disabled"
	enabled = "enabled"
	unknownFutureValue = "unknownFutureValue"


from __future__ import annotations
from enum import StrEnum


class ClickSource(StrEnum):
	unknown = "unknown"
	qrCode = "qrCode"
	phishingUrl = "phishingUrl"
	unknownFutureValue = "unknownFutureValue"


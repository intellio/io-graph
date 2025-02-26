from __future__ import annotations
from enum import Enum


class ClickSource(Enum):
	unknown = "unknown"
	qrCode = "qrCode"
	phishingUrl = "phishingUrl"
	unknownFutureValue = "unknownFutureValue"


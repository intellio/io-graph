from __future__ import annotations
from enum import StrEnum


class WiFiProxySetting(StrEnum):
	none = "none"
	manual = "manual"
	automatic = "automatic"
	unknownFutureValue = "unknownFutureValue"


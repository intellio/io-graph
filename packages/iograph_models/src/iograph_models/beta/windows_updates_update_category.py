from __future__ import annotations
from enum import StrEnum


class WindowsUpdatesUpdateCategory(StrEnum):
	feature = "feature"
	quality = "quality"
	unknownFutureValue = "unknownFutureValue"
	driver = "driver"


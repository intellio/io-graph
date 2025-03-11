from __future__ import annotations
from enum import StrEnum


class MediaState(StrEnum):
	active = "active"
	inactive = "inactive"
	unknownFutureValue = "unknownFutureValue"


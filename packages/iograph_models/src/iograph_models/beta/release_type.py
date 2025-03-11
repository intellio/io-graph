from __future__ import annotations
from enum import StrEnum


class ReleaseType(StrEnum):
	preview = "preview"
	generallyAvailable = "generallyAvailable"
	unknownFutureValue = "unknownFutureValue"


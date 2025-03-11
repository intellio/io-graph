from __future__ import annotations
from enum import StrEnum


class IngestionSource(StrEnum):
	unknown = "unknown"
	custom = "custom"
	builtIn = "builtIn"
	unknownFutureValue = "unknownFutureValue"


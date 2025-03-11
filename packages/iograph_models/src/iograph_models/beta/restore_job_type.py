from __future__ import annotations
from enum import StrEnum


class RestoreJobType(StrEnum):
	standard = "standard"
	bulk = "bulk"
	unknownFutureValue = "unknownFutureValue"


from __future__ import annotations
from enum import StrEnum


class RestorePointPreference(StrEnum):
	latest = "latest"
	oldest = "oldest"
	unknownFutureValue = "unknownFutureValue"


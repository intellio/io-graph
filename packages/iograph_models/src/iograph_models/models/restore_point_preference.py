from __future__ import annotations
from enum import Enum


class RestorePointPreference(Enum):
	latest = "latest"
	oldest = "oldest"
	unknownFutureValue = "unknownFutureValue"


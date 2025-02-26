from __future__ import annotations
from enum import Enum


class SearchAlterationType(Enum):
	suggestion = "suggestion"
	modification = "modification"
	unknownFutureValue = "unknownFutureValue"


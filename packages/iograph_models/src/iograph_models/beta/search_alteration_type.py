from __future__ import annotations
from enum import StrEnum


class SearchAlterationType(StrEnum):
	suggestion = "suggestion"
	modification = "modification"
	unknownFutureValue = "unknownFutureValue"


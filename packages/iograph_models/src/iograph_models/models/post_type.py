from __future__ import annotations
from enum import StrEnum


class PostType(StrEnum):
	regular = "regular"
	quick = "quick"
	strategic = "strategic"
	unknownFutureValue = "unknownFutureValue"


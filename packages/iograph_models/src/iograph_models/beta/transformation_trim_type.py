from __future__ import annotations
from enum import StrEnum


class TransformationTrimType(StrEnum):
	leading = "leading"
	trailing = "trailing"
	leadingAndTrailing = "leadingAndTrailing"
	unknownFutureValue = "unknownFutureValue"


from __future__ import annotations
from enum import StrEnum


class LabelKind(StrEnum):
	all = "all"
	enumerated = "enumerated"
	unknownFutureValue = "unknownFutureValue"


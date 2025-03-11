from __future__ import annotations
from enum import StrEnum


class TransformationExtractType(StrEnum):
	prefix = "prefix"
	suffix = "suffix"
	unknownFutureValue = "unknownFutureValue"


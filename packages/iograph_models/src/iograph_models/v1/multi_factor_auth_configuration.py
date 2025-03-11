from __future__ import annotations
from enum import StrEnum


class MultiFactorAuthConfiguration(StrEnum):
	notRequired = "notRequired"
	required = "required"
	unknownFutureValue = "unknownFutureValue"


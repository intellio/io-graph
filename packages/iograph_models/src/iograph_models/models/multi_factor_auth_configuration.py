from __future__ import annotations
from enum import Enum


class MultiFactorAuthConfiguration(Enum):
	notRequired = "notRequired"
	required = "required"
	unknownFutureValue = "unknownFutureValue"


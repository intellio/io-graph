from __future__ import annotations
from enum import StrEnum


class FeatureTargetType(StrEnum):
	group = "group"
	administrativeUnit = "administrativeUnit"
	role = "role"
	unknownFutureValue = "unknownFutureValue"


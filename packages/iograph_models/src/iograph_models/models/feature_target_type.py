from __future__ import annotations
from enum import Enum


class FeatureTargetType(Enum):
	group = "group"
	administrativeUnit = "administrativeUnit"
	role = "role"
	unknownFutureValue = "unknownFutureValue"


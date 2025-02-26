from __future__ import annotations
from enum import Enum


class FeatureType(Enum):
	registration = "registration"
	reset = "reset"
	unknownFutureValue = "unknownFutureValue"


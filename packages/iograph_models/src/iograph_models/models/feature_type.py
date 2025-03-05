from __future__ import annotations
from enum import StrEnum


class FeatureType(StrEnum):
	registration = "registration"
	reset = "reset"
	unknownFutureValue = "unknownFutureValue"


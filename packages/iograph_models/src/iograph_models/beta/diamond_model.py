from __future__ import annotations
from enum import StrEnum


class DiamondModel(StrEnum):
	unknown = "unknown"
	adversary = "adversary"
	capability = "capability"
	infrastructure = "infrastructure"
	victim = "victim"
	unknownFutureValue = "unknownFutureValue"


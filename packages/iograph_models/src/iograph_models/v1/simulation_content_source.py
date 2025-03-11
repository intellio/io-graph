from __future__ import annotations
from enum import StrEnum


class SimulationContentSource(StrEnum):
	unknown = "unknown"
	global_ = "global_"
	tenant = "tenant"
	unknownFutureValue = "unknownFutureValue"


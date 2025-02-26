from __future__ import annotations
from enum import Enum


class SimulationContentSource(Enum):
	unknown = "unknown"
	global_ = "global_"
	tenant = "tenant"
	unknownFutureValue = "unknownFutureValue"


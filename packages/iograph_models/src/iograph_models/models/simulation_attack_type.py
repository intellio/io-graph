from __future__ import annotations
from enum import Enum


class SimulationAttackType(Enum):
	unknown = "unknown"
	social = "social"
	cloud = "cloud"
	endpoint = "endpoint"
	unknownFutureValue = "unknownFutureValue"


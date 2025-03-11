from __future__ import annotations
from enum import StrEnum


class SimulationAttackType(StrEnum):
	unknown = "unknown"
	social = "social"
	cloud = "cloud"
	endpoint = "endpoint"
	unknownFutureValue = "unknownFutureValue"


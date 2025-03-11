from __future__ import annotations
from enum import StrEnum


class HealthState(StrEnum):
	unknown = "unknown"
	healthy = "healthy"
	unhealthy = "unhealthy"


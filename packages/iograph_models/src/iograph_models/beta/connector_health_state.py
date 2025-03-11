from __future__ import annotations
from enum import StrEnum


class ConnectorHealthState(StrEnum):
	healthy = "healthy"
	warning = "warning"
	unhealthy = "unhealthy"
	unknown = "unknown"


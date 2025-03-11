from __future__ import annotations
from enum import StrEnum


class CloudPcExternalPartnerStatus(StrEnum):
	notAvailable = "notAvailable"
	available = "available"
	healthy = "healthy"
	unhealthy = "unhealthy"
	unknownFutureValue = "unknownFutureValue"


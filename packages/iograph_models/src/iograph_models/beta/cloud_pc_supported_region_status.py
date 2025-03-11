from __future__ import annotations
from enum import StrEnum


class CloudPcSupportedRegionStatus(StrEnum):
	available = "available"
	restricted = "restricted"
	unavailable = "unavailable"
	unknownFutureValue = "unknownFutureValue"


from __future__ import annotations
from enum import StrEnum


class SecurityGoogleCloudLocationType(StrEnum):
	unknown = "unknown"
	regional = "regional"
	zonal = "zonal"
	global_ = "global_"
	unknownFutureValue = "unknownFutureValue"


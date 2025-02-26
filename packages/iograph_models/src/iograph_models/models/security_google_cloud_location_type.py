from __future__ import annotations
from enum import Enum


class SecurityGoogleCloudLocationType(Enum):
	unknown = "unknown"
	regional = "regional"
	zonal = "zonal"
	global_ = "global_"
	unknownFutureValue = "unknownFutureValue"


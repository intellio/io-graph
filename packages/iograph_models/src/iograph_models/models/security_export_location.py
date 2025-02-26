from __future__ import annotations
from enum import Enum


class SecurityExportLocation(Enum):
	responsiveLocations = "responsiveLocations"
	nonresponsiveLocations = "nonresponsiveLocations"
	unknownFutureValue = "unknownFutureValue"


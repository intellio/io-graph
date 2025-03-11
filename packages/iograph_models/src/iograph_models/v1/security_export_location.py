from __future__ import annotations
from enum import StrEnum


class SecurityExportLocation(StrEnum):
	responsiveLocations = "responsiveLocations"
	nonresponsiveLocations = "nonresponsiveLocations"
	unknownFutureValue = "unknownFutureValue"


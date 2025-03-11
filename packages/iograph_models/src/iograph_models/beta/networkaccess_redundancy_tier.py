from __future__ import annotations
from enum import StrEnum


class NetworkaccessRedundancyTier(StrEnum):
	noRedundancy = "noRedundancy"
	zoneRedundancy = "zoneRedundancy"
	unknownFutureValue = "unknownFutureValue"


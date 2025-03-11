from __future__ import annotations
from enum import StrEnum


class MacOSSoftwareUpdateDelayPolicy(StrEnum):
	none = "none"
	delayOSUpdateVisibility = "delayOSUpdateVisibility"
	delayAppUpdateVisibility = "delayAppUpdateVisibility"
	unknownFutureValue = "unknownFutureValue"
	delayMajorOsUpdateVisibility = "delayMajorOsUpdateVisibility"


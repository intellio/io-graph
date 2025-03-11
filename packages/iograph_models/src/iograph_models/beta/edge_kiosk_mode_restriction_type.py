from __future__ import annotations
from enum import StrEnum


class EdgeKioskModeRestrictionType(StrEnum):
	notConfigured = "notConfigured"
	digitalSignage = "digitalSignage"
	normalMode = "normalMode"
	publicBrowsingSingleApp = "publicBrowsingSingleApp"
	publicBrowsingMultiApp = "publicBrowsingMultiApp"


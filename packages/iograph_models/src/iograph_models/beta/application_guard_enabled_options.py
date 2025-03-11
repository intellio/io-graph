from __future__ import annotations
from enum import StrEnum


class ApplicationGuardEnabledOptions(StrEnum):
	notConfigured = "notConfigured"
	enabledForEdge = "enabledForEdge"
	enabledForOffice = "enabledForOffice"
	enabledForEdgeAndOffice = "enabledForEdgeAndOffice"


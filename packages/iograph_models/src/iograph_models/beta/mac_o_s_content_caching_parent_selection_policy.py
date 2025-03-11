from __future__ import annotations
from enum import StrEnum


class MacOSContentCachingParentSelectionPolicy(StrEnum):
	notConfigured = "notConfigured"
	roundRobin = "roundRobin"
	firstAvailable = "firstAvailable"
	urlPathHash = "urlPathHash"
	random = "random"
	stickyAvailable = "stickyAvailable"


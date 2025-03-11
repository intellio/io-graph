from __future__ import annotations
from enum import StrEnum


class OfficeUpdateChannel(StrEnum):
	none = "none"
	current = "current"
	deferred = "deferred"
	firstReleaseCurrent = "firstReleaseCurrent"
	firstReleaseDeferred = "firstReleaseDeferred"
	monthlyEnterprise = "monthlyEnterprise"


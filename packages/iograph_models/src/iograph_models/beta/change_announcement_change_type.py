from __future__ import annotations
from enum import StrEnum


class ChangeAnnouncementChangeType(StrEnum):
	breakingChange = "breakingChange"
	deprecation = "deprecation"
	endOfSupport = "endOfSupport"
	featureChange = "featureChange"
	other = "other"
	retirement = "retirement"
	securityIncident = "securityIncident"
	uxChange = "uxChange"
	unknownFutureValue = "unknownFutureValue"


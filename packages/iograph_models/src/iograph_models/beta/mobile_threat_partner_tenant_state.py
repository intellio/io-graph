from __future__ import annotations
from enum import StrEnum


class MobileThreatPartnerTenantState(StrEnum):
	unavailable = "unavailable"
	available = "available"
	enabled = "enabled"
	unresponsive = "unresponsive"
	notSetUp = "notSetUp"
	error = "error"
	unknownFutureValue = "unknownFutureValue"


from __future__ import annotations
from enum import Enum


class MobileThreatPartnerTenantState(Enum):
	unavailable = "unavailable"
	available = "available"
	enabled = "enabled"
	unresponsive = "unresponsive"
	unknownFutureValue = "unknownFutureValue"


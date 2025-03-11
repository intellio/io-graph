from __future__ import annotations
from enum import StrEnum


class PartnerSecuritySecurityAlertStatus(StrEnum):
	active = "active"
	resolved = "resolved"
	investigating = "investigating"
	unknownFutureValue = "unknownFutureValue"


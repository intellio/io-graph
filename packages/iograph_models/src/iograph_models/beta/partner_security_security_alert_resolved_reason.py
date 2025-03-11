from __future__ import annotations
from enum import StrEnum


class PartnerSecuritySecurityAlertResolvedReason(StrEnum):
	legitimate = "legitimate"
	ignore = "ignore"
	fraud = "fraud"
	unknownFutureValue = "unknownFutureValue"


from __future__ import annotations
from enum import StrEnum


class DisableReason(StrEnum):
	none = "none"
	invalidBillingProfile = "invalidBillingProfile"
	userRequested = "userRequested"
	unknownFutureValue = "unknownFutureValue"


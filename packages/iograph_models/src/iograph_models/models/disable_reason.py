from __future__ import annotations
from enum import Enum


class DisableReason(Enum):
	none = "none"
	invalidBillingProfile = "invalidBillingProfile"
	userRequested = "userRequested"
	unknownFutureValue = "unknownFutureValue"


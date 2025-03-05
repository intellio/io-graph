from __future__ import annotations
from enum import StrEnum


class AccessPackageRequestState(StrEnum):
	submitted = "submitted"
	pendingApproval = "pendingApproval"
	delivering = "delivering"
	delivered = "delivered"
	deliveryFailed = "deliveryFailed"
	denied = "denied"
	scheduled = "scheduled"
	canceled = "canceled"
	partiallyDelivered = "partiallyDelivered"
	unknownFutureValue = "unknownFutureValue"


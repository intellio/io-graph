from __future__ import annotations
from enum import Enum


class AccessPackageRequestState(Enum):
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


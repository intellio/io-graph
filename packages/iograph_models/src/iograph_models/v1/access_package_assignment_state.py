from __future__ import annotations
from enum import StrEnum


class AccessPackageAssignmentState(StrEnum):
	delivering = "delivering"
	partiallyDelivered = "partiallyDelivered"
	delivered = "delivered"
	expired = "expired"
	deliveryFailed = "deliveryFailed"
	unknownFutureValue = "unknownFutureValue"


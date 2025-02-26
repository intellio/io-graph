from __future__ import annotations
from enum import Enum


class AccessPackageAssignmentState(Enum):
	delivering = "delivering"
	partiallyDelivered = "partiallyDelivered"
	delivered = "delivered"
	expired = "expired"
	deliveryFailed = "deliveryFailed"
	unknownFutureValue = "unknownFutureValue"


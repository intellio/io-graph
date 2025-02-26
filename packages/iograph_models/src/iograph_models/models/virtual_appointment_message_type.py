from __future__ import annotations
from enum import Enum


class VirtualAppointmentMessageType(Enum):
	confirmation = "confirmation"
	reschedule = "reschedule"
	cancellation = "cancellation"
	unknownFutureValue = "unknownFutureValue"


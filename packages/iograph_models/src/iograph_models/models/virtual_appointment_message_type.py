from __future__ import annotations
from enum import StrEnum


class VirtualAppointmentMessageType(StrEnum):
	confirmation = "confirmation"
	reschedule = "reschedule"
	cancellation = "cancellation"
	unknownFutureValue = "unknownFutureValue"


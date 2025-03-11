from __future__ import annotations
from enum import StrEnum


class MeetingRegistrantStatus(StrEnum):
	registered = "registered"
	canceled = "canceled"
	processing = "processing"
	unknownFutureValue = "unknownFutureValue"


from __future__ import annotations
from enum import StrEnum


class OnlineMeetingRole(StrEnum):
	attendee = "attendee"
	presenter = "presenter"
	producer = "producer"
	unknownFutureValue = "unknownFutureValue"
	coorganizer = "coorganizer"


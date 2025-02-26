from __future__ import annotations
from enum import Enum


class OnlineMeetingRole(Enum):
	attendee = "attendee"
	presenter = "presenter"
	unknownFutureValue = "unknownFutureValue"
	producer = "producer"
	coorganizer = "coorganizer"


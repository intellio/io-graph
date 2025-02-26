from __future__ import annotations
from enum import Enum


class ScheduleChangeRequestActor(Enum):
	sender = "sender"
	recipient = "recipient"
	manager = "manager"
	system = "system"
	unknownFutureValue = "unknownFutureValue"


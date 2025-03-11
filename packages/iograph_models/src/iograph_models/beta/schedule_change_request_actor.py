from __future__ import annotations
from enum import StrEnum


class ScheduleChangeRequestActor(StrEnum):
	sender = "sender"
	recipient = "recipient"
	manager = "manager"
	system = "system"
	unknownFutureValue = "unknownFutureValue"


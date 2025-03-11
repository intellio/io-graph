from __future__ import annotations
from enum import StrEnum


class InitiatorType(StrEnum):
	user = "user"
	application = "application"
	system = "system"
	unknownFutureValue = "unknownFutureValue"


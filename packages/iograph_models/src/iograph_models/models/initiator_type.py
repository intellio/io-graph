from __future__ import annotations
from enum import Enum


class InitiatorType(Enum):
	user = "user"
	application = "application"
	system = "system"
	unknownFutureValue = "unknownFutureValue"


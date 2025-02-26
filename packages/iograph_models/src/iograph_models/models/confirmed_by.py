from __future__ import annotations
from enum import Enum


class ConfirmedBy(Enum):
	none = "none"
	user = "user"
	manager = "manager"
	unknownFutureValue = "unknownFutureValue"


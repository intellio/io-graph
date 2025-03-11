from __future__ import annotations
from enum import StrEnum


class ConfirmedBy(StrEnum):
	none = "none"
	user = "user"
	manager = "manager"
	unknownFutureValue = "unknownFutureValue"


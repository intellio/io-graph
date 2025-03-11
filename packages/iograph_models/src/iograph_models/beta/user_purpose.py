from __future__ import annotations
from enum import StrEnum


class UserPurpose(StrEnum):
	unknown = "unknown"
	user = "user"
	linked = "linked"
	shared = "shared"
	room = "room"
	equipment = "equipment"
	others = "others"
	unknownFutureValue = "unknownFutureValue"


from __future__ import annotations
from enum import StrEnum


class UserPurpose(StrEnum):
	user = "user"
	linked = "linked"
	shared = "shared"
	room = "room"
	equipment = "equipment"
	others = "others"
	unknownFutureValue = "unknownFutureValue"


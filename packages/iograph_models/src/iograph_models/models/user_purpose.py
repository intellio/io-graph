from __future__ import annotations
from enum import Enum


class UserPurpose(Enum):
	user = "user"
	linked = "linked"
	shared = "shared"
	room = "room"
	equipment = "equipment"
	others = "others"
	unknownFutureValue = "unknownFutureValue"


from __future__ import annotations
from enum import StrEnum


class AclType(StrEnum):
	user = "user"
	group = "group"
	everyone = "everyone"
	everyoneExceptGuests = "everyoneExceptGuests"
	externalGroup = "externalGroup"
	unknownFutureValue = "unknownFutureValue"


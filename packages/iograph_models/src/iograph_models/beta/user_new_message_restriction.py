from __future__ import annotations
from enum import StrEnum


class UserNewMessageRestriction(StrEnum):
	everyone = "everyone"
	everyoneExceptGuests = "everyoneExceptGuests"
	moderators = "moderators"
	unknownFutureValue = "unknownFutureValue"


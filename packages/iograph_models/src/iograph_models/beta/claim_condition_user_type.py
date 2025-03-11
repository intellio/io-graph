from __future__ import annotations
from enum import StrEnum


class ClaimConditionUserType(StrEnum):
	any = "any"
	members = "members"
	allGuests = "allGuests"
	aadGuests = "aadGuests"
	externalGuests = "externalGuests"
	unknownFutureValue = "unknownFutureValue"


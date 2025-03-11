from __future__ import annotations
from enum import StrEnum


class AllowInvitesFrom(StrEnum):
	none = "none"
	adminsAndGuestInviters = "adminsAndGuestInviters"
	adminsGuestInvitersAndAllMembers = "adminsGuestInvitersAndAllMembers"
	everyone = "everyone"
	unknownFutureValue = "unknownFutureValue"


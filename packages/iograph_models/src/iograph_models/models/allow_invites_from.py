from __future__ import annotations
from enum import Enum


class AllowInvitesFrom(Enum):
	none = "none"
	adminsAndGuestInviters = "adminsAndGuestInviters"
	adminsGuestInvitersAndAllMembers = "adminsGuestInvitersAndAllMembers"
	everyone = "everyone"
	unknownFutureValue = "unknownFutureValue"


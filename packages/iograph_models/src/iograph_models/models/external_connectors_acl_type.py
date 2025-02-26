from __future__ import annotations
from enum import Enum


class ExternalConnectorsAclType(Enum):
	user = "user"
	group = "group"
	everyone = "everyone"
	everyoneExceptGuests = "everyoneExceptGuests"
	externalGroup = "externalGroup"
	unknownFutureValue = "unknownFutureValue"


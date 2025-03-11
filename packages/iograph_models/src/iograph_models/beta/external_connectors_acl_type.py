from __future__ import annotations
from enum import StrEnum


class ExternalConnectorsAclType(StrEnum):
	user = "user"
	group = "group"
	everyone = "everyone"
	everyoneExceptGuests = "everyoneExceptGuests"
	externalGroup = "externalGroup"
	unknownFutureValue = "unknownFutureValue"


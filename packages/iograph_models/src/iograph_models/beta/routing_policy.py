from __future__ import annotations
from enum import StrEnum


class RoutingPolicy(StrEnum):
	none = "none"
	noMissedCall = "noMissedCall"
	disableForwardingExceptPhone = "disableForwardingExceptPhone"
	disableForwarding = "disableForwarding"
	preferSkypeForBusiness = "preferSkypeForBusiness"
	unknownFutureValue = "unknownFutureValue"


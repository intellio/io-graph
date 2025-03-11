from __future__ import annotations
from enum import StrEnum


class PrivateNetworkDestinationType(StrEnum):
	ipAddress = "ipAddress"
	ipRange = "ipRange"
	ipRangeCidr = "ipRangeCidr"
	fqdn = "fqdn"
	dnsSuffix = "dnsSuffix"
	unknownFutureValue = "unknownFutureValue"


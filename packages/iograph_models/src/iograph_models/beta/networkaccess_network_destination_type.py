from __future__ import annotations
from enum import StrEnum


class NetworkaccessNetworkDestinationType(StrEnum):
	url = "url"
	fqdn = "fqdn"
	ipAddress = "ipAddress"
	ipRange = "ipRange"
	ipSubnet = "ipSubnet"
	webCategory = "webCategory"
	unknownFutureValue = "unknownFutureValue"


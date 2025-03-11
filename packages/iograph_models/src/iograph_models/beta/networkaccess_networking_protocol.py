from __future__ import annotations
from enum import StrEnum


class NetworkaccessNetworkingProtocol(StrEnum):
	ip = "ip"
	icmp = "icmp"
	igmp = "igmp"
	ggp = "ggp"
	ipv4 = "ipv4"
	tcp = "tcp"
	pup = "pup"
	udp = "udp"
	idp = "idp"
	ipv6 = "ipv6"
	ipv6RoutingHeader = "ipv6RoutingHeader"
	ipv6FragmentHeader = "ipv6FragmentHeader"
	ipSecEncapsulatingSecurityPayload = "ipSecEncapsulatingSecurityPayload"
	ipSecAuthenticationHeader = "ipSecAuthenticationHeader"
	icmpV6 = "icmpV6"
	ipv6NoNextHeader = "ipv6NoNextHeader"
	ipv6DestinationOptions = "ipv6DestinationOptions"
	nd = "nd"
	ipx = "ipx"
	raw = "raw"
	spx = "spx"
	spxII = "spxII"
	unknownFutureValue = "unknownFutureValue"


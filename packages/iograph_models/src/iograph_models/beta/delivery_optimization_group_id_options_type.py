from __future__ import annotations
from enum import StrEnum


class DeliveryOptimizationGroupIdOptionsType(StrEnum):
	notConfigured = "notConfigured"
	adSite = "adSite"
	authenticatedDomainSid = "authenticatedDomainSid"
	dhcpUserOption = "dhcpUserOption"
	dnsSuffix = "dnsSuffix"


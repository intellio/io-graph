from __future__ import annotations
from enum import StrEnum


class MacOSContentCachingClientPolicy(StrEnum):
	notConfigured = "notConfigured"
	clientsInLocalNetwork = "clientsInLocalNetwork"
	clientsWithSamePublicIpAddress = "clientsWithSamePublicIpAddress"
	clientsInCustomLocalNetworks = "clientsInCustomLocalNetworks"
	clientsInCustomLocalNetworksWithFallback = "clientsInCustomLocalNetworksWithFallback"


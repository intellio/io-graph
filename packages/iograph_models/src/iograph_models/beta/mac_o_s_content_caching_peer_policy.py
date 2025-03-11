from __future__ import annotations
from enum import StrEnum


class MacOSContentCachingPeerPolicy(StrEnum):
	notConfigured = "notConfigured"
	peersInLocalNetwork = "peersInLocalNetwork"
	peersWithSamePublicIpAddress = "peersWithSamePublicIpAddress"
	peersInCustomLocalNetworks = "peersInCustomLocalNetworks"


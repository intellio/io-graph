from __future__ import annotations
from enum import StrEnum


class VpnProviderType(StrEnum):
	notConfigured = "notConfigured"
	appProxy = "appProxy"
	packetTunnel = "packetTunnel"


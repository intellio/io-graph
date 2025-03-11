from __future__ import annotations
from enum import StrEnum


class NetworkaccessRemoteNetworkStatus(StrEnum):
	tunnelDisconnected = "tunnelDisconnected"
	tunnelConnected = "tunnelConnected"
	bgpDisconnected = "bgpDisconnected"
	bgpConnected = "bgpConnected"
	remoteNetworkAlive = "remoteNetworkAlive"
	unknownFutureValue = "unknownFutureValue"


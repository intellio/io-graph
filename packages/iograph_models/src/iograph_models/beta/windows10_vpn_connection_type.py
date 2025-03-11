from __future__ import annotations
from enum import StrEnum


class Windows10VpnConnectionType(StrEnum):
	pulseSecure = "pulseSecure"
	f5EdgeClient = "f5EdgeClient"
	dellSonicWallMobileConnect = "dellSonicWallMobileConnect"
	checkPointCapsuleVpn = "checkPointCapsuleVpn"
	automatic = "automatic"
	ikEv2 = "ikEv2"
	l2tp = "l2tp"
	pptp = "pptp"
	citrix = "citrix"
	paloAltoGlobalProtect = "paloAltoGlobalProtect"
	ciscoAnyConnect = "ciscoAnyConnect"
	unknownFutureValue = "unknownFutureValue"
	microsoftTunnel = "microsoftTunnel"


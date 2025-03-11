from __future__ import annotations
from enum import StrEnum


class AndroidWorkProfileVpnConnectionType(StrEnum):
	ciscoAnyConnect = "ciscoAnyConnect"
	pulseSecure = "pulseSecure"
	f5EdgeClient = "f5EdgeClient"
	dellSonicWallMobileConnect = "dellSonicWallMobileConnect"
	checkPointCapsuleVpn = "checkPointCapsuleVpn"
	citrix = "citrix"
	paloAltoGlobalProtect = "paloAltoGlobalProtect"
	microsoftTunnel = "microsoftTunnel"
	netMotionMobility = "netMotionMobility"
	microsoftProtect = "microsoftProtect"


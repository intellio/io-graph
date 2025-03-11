from __future__ import annotations
from enum import StrEnum


class AndroidVpnConnectionType(StrEnum):
	ciscoAnyConnect = "ciscoAnyConnect"
	pulseSecure = "pulseSecure"
	f5EdgeClient = "f5EdgeClient"
	dellSonicWallMobileConnect = "dellSonicWallMobileConnect"
	checkPointCapsuleVpn = "checkPointCapsuleVpn"
	citrix = "citrix"
	microsoftTunnel = "microsoftTunnel"
	netMotionMobility = "netMotionMobility"
	microsoftProtect = "microsoftProtect"


from __future__ import annotations
from enum import StrEnum


class AndroidForWorkVpnConnectionType(StrEnum):
	ciscoAnyConnect = "ciscoAnyConnect"
	pulseSecure = "pulseSecure"
	f5EdgeClient = "f5EdgeClient"
	dellSonicWallMobileConnect = "dellSonicWallMobileConnect"
	checkPointCapsuleVpn = "checkPointCapsuleVpn"
	citrix = "citrix"


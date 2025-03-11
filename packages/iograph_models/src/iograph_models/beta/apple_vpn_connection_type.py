from __future__ import annotations
from enum import StrEnum


class AppleVpnConnectionType(StrEnum):
	ciscoAnyConnect = "ciscoAnyConnect"
	pulseSecure = "pulseSecure"
	f5EdgeClient = "f5EdgeClient"
	dellSonicWallMobileConnect = "dellSonicWallMobileConnect"
	checkPointCapsuleVpn = "checkPointCapsuleVpn"
	customVpn = "customVpn"
	ciscoIPSec = "ciscoIPSec"
	citrix = "citrix"
	ciscoAnyConnectV2 = "ciscoAnyConnectV2"
	paloAltoGlobalProtect = "paloAltoGlobalProtect"
	zscalerPrivateAccess = "zscalerPrivateAccess"
	f5Access2018 = "f5Access2018"
	citrixSso = "citrixSso"
	paloAltoGlobalProtectV2 = "paloAltoGlobalProtectV2"
	ikEv2 = "ikEv2"
	alwaysOn = "alwaysOn"
	microsoftTunnel = "microsoftTunnel"
	netMotionMobility = "netMotionMobility"
	microsoftProtect = "microsoftProtect"


from __future__ import annotations
from enum import StrEnum


class AospDeviceOwnerWiFiSecurityType(StrEnum):
	open = "open"
	wep = "wep"
	wpaPersonal = "wpaPersonal"
	wpaEnterprise = "wpaEnterprise"


from __future__ import annotations
from enum import StrEnum


class AndroidDeviceOwnerWiFiSecurityType(StrEnum):
	open = "open"
	wep = "wep"
	wpaPersonal = "wpaPersonal"
	wpaEnterprise = "wpaEnterprise"


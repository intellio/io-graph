from __future__ import annotations
from enum import StrEnum


class AndroidWiFiSecurityType(StrEnum):
	open = "open"
	wpaEnterprise = "wpaEnterprise"
	wpa2Enterprise = "wpa2Enterprise"
	wep = "wep"
	wpaPersonal = "wpaPersonal"
	unknownFutureValue = "unknownFutureValue"


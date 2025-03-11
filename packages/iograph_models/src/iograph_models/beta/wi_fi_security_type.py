from __future__ import annotations
from enum import StrEnum


class WiFiSecurityType(StrEnum):
	open = "open"
	wpaPersonal = "wpaPersonal"
	wpaEnterprise = "wpaEnterprise"
	wep = "wep"
	wpa2Personal = "wpa2Personal"
	wpa2Enterprise = "wpa2Enterprise"


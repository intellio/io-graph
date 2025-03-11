from __future__ import annotations
from enum import StrEnum


class VpnServiceExceptionAction(StrEnum):
	forceTrafficViaVPN = "forceTrafficViaVPN"
	allowTrafficOutside = "allowTrafficOutside"
	dropTraffic = "dropTraffic"


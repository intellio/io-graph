from __future__ import annotations
from enum import StrEnum


class VpnClientAuthenticationType(StrEnum):
	userAuthentication = "userAuthentication"
	deviceAuthentication = "deviceAuthentication"


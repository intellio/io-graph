from __future__ import annotations
from enum import StrEnum


class DeviceManagementExchangeAccessLevel(StrEnum):
	none = "none"
	allow = "allow"
	block = "block"
	quarantine = "quarantine"


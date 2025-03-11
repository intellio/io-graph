from __future__ import annotations
from enum import StrEnum


class Windows10VpnProfileTarget(StrEnum):
	user = "user"
	device = "device"
	autoPilotDevice = "autoPilotDevice"


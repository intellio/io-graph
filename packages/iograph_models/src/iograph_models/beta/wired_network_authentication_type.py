from __future__ import annotations
from enum import StrEnum


class WiredNetworkAuthenticationType(StrEnum):
	none = "none"
	user = "user"
	machine = "machine"
	machineOrUser = "machineOrUser"
	guest = "guest"
	unknownFutureValue = "unknownFutureValue"


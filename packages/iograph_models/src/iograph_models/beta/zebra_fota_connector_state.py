from __future__ import annotations
from enum import StrEnum


class ZebraFotaConnectorState(StrEnum):
	none = "none"
	connected = "connected"
	disconnected = "disconnected"
	unknownFutureValue = "unknownFutureValue"


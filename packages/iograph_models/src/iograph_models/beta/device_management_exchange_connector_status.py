from __future__ import annotations
from enum import StrEnum


class DeviceManagementExchangeConnectorStatus(StrEnum):
	none = "none"
	connectionPending = "connectionPending"
	connected = "connected"
	disconnected = "disconnected"
	unknownFutureValue = "unknownFutureValue"


from __future__ import annotations
from enum import Enum


class DeviceManagementExchangeConnectorStatus(Enum):
	none = "none"
	connectionPending = "connectionPending"
	connected = "connected"
	disconnected = "disconnected"
	unknownFutureValue = "unknownFutureValue"


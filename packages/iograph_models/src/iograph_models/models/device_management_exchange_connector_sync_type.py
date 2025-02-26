from __future__ import annotations
from enum import Enum


class DeviceManagementExchangeConnectorSyncType(Enum):
	fullSync = "fullSync"
	deltaSync = "deltaSync"


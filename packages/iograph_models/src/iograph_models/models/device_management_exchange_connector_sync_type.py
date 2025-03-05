from __future__ import annotations
from enum import StrEnum


class DeviceManagementExchangeConnectorSyncType(StrEnum):
	fullSync = "fullSync"
	deltaSync = "deltaSync"


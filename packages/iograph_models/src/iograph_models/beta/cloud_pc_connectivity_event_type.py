from __future__ import annotations
from enum import StrEnum


class CloudPcConnectivityEventType(StrEnum):
	unknown = "unknown"
	userConnection = "userConnection"
	userTroubleshooting = "userTroubleshooting"
	deviceHealthCheck = "deviceHealthCheck"
	unknownFutureValue = "unknownFutureValue"


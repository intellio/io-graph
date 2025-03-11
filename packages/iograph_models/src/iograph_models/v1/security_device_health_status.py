from __future__ import annotations
from enum import StrEnum


class SecurityDeviceHealthStatus(StrEnum):
	active = "active"
	inactive = "inactive"
	impairedCommunication = "impairedCommunication"
	noSensorData = "noSensorData"
	noSensorDataImpairedCommunication = "noSensorDataImpairedCommunication"
	unknown = "unknown"
	unknownFutureValue = "unknownFutureValue"


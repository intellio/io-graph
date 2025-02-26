from __future__ import annotations
from enum import Enum


class SecurityDeviceHealthStatus(Enum):
	active = "active"
	inactive = "inactive"
	impairedCommunication = "impairedCommunication"
	noSensorData = "noSensorData"
	noSensorDataImpairedCommunication = "noSensorDataImpairedCommunication"
	unknown = "unknown"
	unknownFutureValue = "unknownFutureValue"


from __future__ import annotations
from enum import StrEnum


class SecurityDeviceAssetIdentifier(StrEnum):
	deviceId = "deviceId"
	deviceName = "deviceName"
	remoteDeviceName = "remoteDeviceName"
	targetDeviceName = "targetDeviceName"
	destinationDeviceName = "destinationDeviceName"
	unknownFutureValue = "unknownFutureValue"


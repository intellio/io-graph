from __future__ import annotations
from enum import StrEnum


class TeamworkDeviceOperationType(StrEnum):
	deviceRestart = "deviceRestart"
	configUpdate = "configUpdate"
	deviceDiagnostics = "deviceDiagnostics"
	softwareUpdate = "softwareUpdate"
	deviceManagementAgentConfigUpdate = "deviceManagementAgentConfigUpdate"
	remoteLogin = "remoteLogin"
	remoteLogout = "remoteLogout"
	unknownFutureValue = "unknownFutureValue"


from __future__ import annotations
from enum import StrEnum


class RegistryHive(StrEnum):
	unknown = "unknown"
	currentConfig = "currentConfig"
	currentUser = "currentUser"
	localMachineSam = "localMachineSam"
	localMachineSecurity = "localMachineSecurity"
	localMachineSoftware = "localMachineSoftware"
	localMachineSystem = "localMachineSystem"
	usersDefault = "usersDefault"
	unknownFutureValue = "unknownFutureValue"

